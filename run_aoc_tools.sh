#!/bin/bash

# Define the image name
IMAGE_NAME="aoc23-tools"

# Load environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Force rebuilding of the image to avoid caching issues
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" != "" ]]; then
  echo "Image $IMAGE_NAME already exists. Removing"
  docker rmi $IMAGE_NAME:latest
fi
echo "Building $IMAGE_NAME image..."
docker build --no-cache -t $IMAGE_NAME .

# Run the Docker container with the specified command
echo "Running Docker container..."
docker run --rm \
    -v "$(pwd)/data:/app/data" \
    -v "$(pwd)/solutions:/app/solutions" \
    -v "$(pwd)":/app/output \
    -e AOC_SESSION="${AOC_SESSION}" \
    $IMAGE_NAME $1

echo "Operation completed successfully." 