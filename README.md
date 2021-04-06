# Posthog for Home Assistant

## Installation

Add the following to your `configuration.yaml`:
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
