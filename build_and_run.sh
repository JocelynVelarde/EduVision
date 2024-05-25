# Build the Docker image
sudo docker build -t combined_image .

# Run the Docker container
sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v /tmp/argus_socket:/tmp/argus_socket --cap-add SYS_PTRACE --device /dev/video0:/dev/video0 combined_image
