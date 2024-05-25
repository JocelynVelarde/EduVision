# Use the Ultralytics Jetson image as the base image
FROM ultralytics/ultralytics:latest-jetson

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install Mediapipe dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    cmake \
    protobuf-compiler \
    libopencv-dev \
    libopencv-core-dev \
    libopencv-highgui-dev \
    libopencv-imgproc-dev \
    libopencv-video-dev \
    libopencv-calib3d-dev \
    python3-opencv

# Clone Mediapipe repository and build
RUN git clone https://github.com/google/mediapipe.git /mediapipe
WORKDIR /mediapipe
RUN sed -i -e 's/cudnn_version == "8.2"/cudnn_version >= "8.2"/' third_party/gpus/cuda/BUILD.tpl
RUN sed -i -e 's/cudnn_version == "8.2"/cudnn_version >= "8.2"/' WORKSPACE
RUN bazel build -c opt --copt -DMESA_EGL_NO_X11_HEADERS mediapipe/examples/desktop/face_detection:face_detection_gpu

# Create a user and set permissions
RUN useradd -m portal_user
RUN chown -R portal_user:portal_user /app /mediapipe
USER portal_user

# Install Python dependencies
RUN pip install --user -r /app/requirements.txt

# Default command to start the container
CMD ["/bin/bash"]

# Set up the environment for display and video device access
ENV DISPLAY=:0
RUN echo "export DISPLAY=:0" >> /home/portal_user/.bashrc
RUN echo "xhost +" >> /home/portal_user/.bashrc
