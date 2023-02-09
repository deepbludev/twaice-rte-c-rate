FROM python:3.11.1-slim-buster

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
# hadolint ignore=DL3008
RUN apt-get update \
  && apt-get -y install --no-install-recommends netcat gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  # install poetry package manager
  && pip3 install poetry==1.3 poethepoet==0.18.1 --no-cache-dir \
  && poetry config virtualenvs.create false

COPY . .
RUN poetry install 

CMD ["poetry", "run", "poe", "serve:dev"]
