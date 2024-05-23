FROM fedora:latest
RUN dnf -y install fedora-messaging python3-fedora-messaging python3-twisted python3-prometheus_client

ADD ./fm-metrics /data 

ENV PYTHONPATH /data/
ENTRYPOINT ["/usr/bin/twistd"]
CMD ["-n", "-y", "/data/app.py"]
EXPOSE 8080
