#!/bin/bash

SEMANTIC_VERSION=$(curl "https://api.github.com/repos/SethAngell/TownsleyComic/tags" | jq -r '.[0].name')
RAW_BASE_URL="https://raw.githubusercontent.com/SethAngell/TownsleyComic/main"

echo Updating townsley to version $SEMANTIC_VERSION

curl $RAW_BASE_URL/.ci/docker-compose.yml -o /home/Townsley/docker-compose.yml
docker-compose pull
docker-compose up -d --build

