#!/bin/sh
# This is bash program to display Hello World
git pull origin develop
docker-compose -f api-staging.yml down
# docker image prune -f
docker-compose -f api-staging.yml build
docker-compose -f api-staging.yml up -d
docker-compose -f api-staging.yml run --rm django python manage.py migrate
# docker-compose -f api-production.yml run --rm django python manage.py collectstatic --noinput
docker update --restart unless-stopped $(docker ps -q)
# docker builder prune -f
# curl https://dev-api.kash4me.com/api/docs/
# curl https://dev-app.kash4me.com/
