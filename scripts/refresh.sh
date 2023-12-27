#!/bin/bash

SEMANTIC_VERSION=$(curl -s "https://api.github.com/repos/SethAngell/TownsleyComic/tags" | jq -r '.[0].name')
RAW_BASE_URL="https://raw.githubusercontent.com/SethAngell/TownsleyComic/main"

echo -e "\e[1;34mUpdating townsley to version $SEMANTIC_VERSION\e[0m"

export SEMANTIC_VERSION="$SEMANTIC_VERSION"

curl -s $RAW_BASE_URL/.ci/docker-compose.yml -o /home/townsley/docker-compose.yml
docker-compose pull
docker-compose up -d --build

echo -e "\e[1;34m✅ All Done ✅\e[0m"
