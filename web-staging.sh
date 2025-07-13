#!/bin/sh
git pull origin develop
docker-compose -f web-staging.yml down
#docker image prune -f
docker-compose -f web-staging.yml build
docker-compose -f web-staging.yml up -d
#docker update --restart unless-stopped $(docker ps -q)
