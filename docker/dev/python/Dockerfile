# FROM python:3.7-alpine

# # install psycopg2 dependencies
# RUN apk update \
#   && apk add postgresql-dev gcc python3-dev musl-dev

FROM python:3.7-slim-stretch

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

WORKDIR /app

COPY ./requirements /app/requirements/

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY . /app

ENTRYPOINT ["/entrypoint.sh"]
