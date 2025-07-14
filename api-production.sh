#!/bin/sh
# This is bash program to display Hello World
git pull origin main
docker-compose -f api-production.yml down
#docker image prune -f
docker-compose -f api-production.yml build
docker-compose -f api-production.yml up -d
docker-compose -f api-production.yml run --rm django python manage.py migrate 
#docker-compose -f api-production.yml run --rm django python manage.py collectstatic --no-input 
docker update --restart unless-stopped $(docker ps -q)
#docker builder prune -f

