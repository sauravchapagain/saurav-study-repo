#!/bin/sh
git pull origin develop
docker-compose -f api-staging.yml down
# docker image prune -f
docker-compose -f api-staging.yml build
docker-compose -f api-staging.yml up -d
docker-compose -f api-staging.yml run --rm django python manage.py migrate
docker-compose -f api-staging.yml run --rm django python manage.py collectstatic --noinput
docker update --restart unless-stopped $(docker ps -q)
