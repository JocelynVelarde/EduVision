#!/bin/bash

# Define the image name
IMAGE_NAME=portal_image

# Build the Docker image
echo "Building the Docker image..."
sudo docker build -t $IMAGE_NAME .

# Check if the container is already running and stop it
if [ "$(sudo docker ps -q -f name=my-container)" ]; then
    echo "Stopping the existing container..."
    sudo docker stop my-container
fi

# Remove the container if it exists
if [ "$(sudo docker ps -aq -f name=my-container)" ]; then
    echo "Removing the existing container..."
    sudo docker rm my-container
fi

# Run the Docker container
echo "Running the Docker container..."
sudo docker run -it --ipc=host --runtime=nvidia --name my-container $IMAGE_NAME

