FROM ultralytics/ultralytics:latest-jetson
WORKDIR /app
COPY . /app
RUN useradd -m portal_user
RUN chown -R portal_user:portal_user /app
USER portal_user
RUN pip install --user -r requirements.txt
CMD ["/bin/bash"]
