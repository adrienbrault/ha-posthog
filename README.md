# Posthog for Home Assistant

## Installation

[HACS](https://hacs.xyz) is the recommended way to install this integration.
Add `https://github.com/adrienbrault/ha-posthog` as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories/).

You'll need to update your `configuration.yaml`:
```
posthog:
  api_key: !secret posthog_api_key
  host: 'https://app.posthog.com' # You can remove this line if you're using app.posthog.com
```

## Notes

Generated using:

```
docker run \
    -it --rm -v $PWD:/app -w /app \
    python:3.8-alpine \
    sh -c 'apk add git ; pip install cookiecutter ; cookiecutter https://github.com/boralyl/cookiecutter-homeassistant-component ; ls -lh'
```
