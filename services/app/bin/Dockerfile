FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# requirements are installed here to ensure they will be cached

COPY ./app/settings/requirements.txt /

RUN pip install -r /requirements.txt

# copy the start script to the container

COPY ./app/bin/start /start

RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy the rest of the files 

COPY . /e2stem.site



