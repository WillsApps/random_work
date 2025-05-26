FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
WORKDIR /random_work
ADD . /random_work
#
RUN apt update
RUN apt full-upgrade -y
RUN apt-get dist-upgrade
RUN apt install libcairo2-dev -y
RUN apt-get install linux-headers-$(uname -r)

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-install-package pynput --no-install-package evdev


# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked