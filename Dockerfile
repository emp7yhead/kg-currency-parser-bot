FROM python:3.10.4-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.2.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin"

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    curl \
    make \
    tree \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version

WORKDIR /code

COPY poetry.lock pyproject.toml Makefile  /code/

RUN make install

COPY . .

RUN make start
