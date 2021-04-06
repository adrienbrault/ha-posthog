from homeassistant import core
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import state as state_helper

from homeassistant.const import (
    EVENT_STATE_CHANGED,
)

import posthog
from posthog.client import Client

DOMAIN = "posthog"

CONF_HOST = "host"
CONF_API_KEY = "api_key"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_API_KEY): cv.string,
                vol.Optional(CONF_HOST): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

def setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Posthog component."""
    host = config[DOMAIN].get(CONF_HOST)
    api_key = config[DOMAIN].get(CONF_API_KEY)

    posthog.project_api_key = api_key
    if host is not None:
        posthog.host = host

    posthog_client = Client(api_key=api_key, host=host)

    async def posthog_event_listener(event):
        """Listen for new messages on the bus."""
        state = event.data.get("new_state")

        if state is None:
            return
        try:
            _state = state_helper.state_as_number(state)
        except ValueError:
            _state = state.state

        attributes = {
            **dict(state.attributes),
            "state": state.state,
            "entity_id": state.entity_id,
            "context": event.context.as_dict(),
            "domain": state.domain,
        }

        user_id = event.context.user_id
        if user_id is not None:
            user = await hass.auth.async_get_user(user_id)
            attributes["$set"] = {
                "name": user.name,
                "is_admin": user.is_admin,
                "is_owner": user.is_owner,
            }

        posthog_client.capture(
            user_id or "unknown",
            event=EVENT_STATE_CHANGED,
            properties=attributes,
            timestamp=event.time_fired,
        )

    hass.bus.listen(EVENT_STATE_CHANGED, posthog_event_listener)

    return True

