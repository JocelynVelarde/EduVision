#!/bin/bash

# Define variables
IMAGE_NAME="combined_ultralytics_mediapipe"
DISPLAY_VAR=":0"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Export DISPLAY variable and allow connections
export DISPLAY=$DISPLAY_VAR
xhost +local:docker

# Find the video devices
VIDEO_DEVICES=$(ls /dev/video* | tr '\n' ' ')

# Run the Docker container
docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /tmp/argus_socket:/tmp/argus_socket \
  --cap-add SYS_PTRACE \
  $(for dev in $VIDEO_DEVICES; do echo --device $dev:$dev; done) \
  $IMAGE_NAME /bin/bash -c 'GLOG_logtostderr=1 bazel-bin/mediapipe/examples/desktop/face_detection/face_detection_gpu --calculator_graph_config_file=mediapipe/graphs/face_detection/face_detection_mobile_gpu.pbtxt'
