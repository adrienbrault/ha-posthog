# Posthog for Home Assistant

## Installation

## Notes

Generated using:

```
docker run \
    -it --rm -v $PWD:/app -w /app \
    python:3.8-alpine \
    sh -c 'apk add git ; pip install cookiecutter ; cookiecutter https://github.com/boralyl/cookiecutter-homeassistant-component ; ls -lh'
```