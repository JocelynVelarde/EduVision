# Use the ultralytics image as the base
FROM ultralytics/ultralytics:latest-jetson

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y x11-xserver-utils && \
    rm -rf /var/lib/apt/lists/*

# Add a new user and change ownership of the app directory
RUN useradd -m portal_user
RUN chown -R portal_user:portal_user /app
USER portal_user

# Install Python dependencies
RUN pip install --user -r requirements.txt

# Set environment variables
ENV DISPLAY=:0

# Allow connections to the X server from any host
RUN xhost +

# Define the command to run the face detection example
CMD ["/bin/bash", "-c", "GLOG_logtostderr=1 bazel-bin/mediapipe/examples/desktop/face_detection/face_detection_gpu --calculator_graph_config_file=mediapipe/graphs/face_detection/face_detection_mobile_gpu.pbtxt"]
