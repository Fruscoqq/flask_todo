#!/bin/bash

echo "Deploy stage"

scp docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh jenkins@swarm-manager \
 DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
 DATABASE_URI=$DATABASE_URI \
 SECRET_KEY=$SECRET_KEY \
 docker stack deploy --compose-file docker-compose.yaml trackhub