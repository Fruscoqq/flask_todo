#!/bin/bash

echo "Deploy stage"

ssh jenkins@SwarmManager docker stack deploy --compose-file docker-compose.yaml trackhub