FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
WORKDIR /app
ADD . /app
ADD ../../.env /app/.env
ADD ../utils/. /app/utils/.

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-install-package pynput --no-install-package evdev


# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked