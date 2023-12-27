#!/bin/bash

SEMANTIC_VERSION=$(curl "https://api.github.com/repos/SethAngell/TownsleyComic/tags" | jq -r '.[0].name')

echo Updating townsley to version $SEMANTIC_VERSION
docker-compose pull
docker-compose up -d --build

