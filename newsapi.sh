#!/bin/bash

KEY=$(cat pass.yml | /usr/local/bin/yq e .newsapi.key -)

curl https://newsapi.org/v2/top-headlines -G \
  -d country=us \
  -d apiKey="$KEY" | jq . > news.json
