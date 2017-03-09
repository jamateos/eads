#!/bin/bash
docker build -t eads-demo-pumba-kill .
docker run -it -v /var/run/docker.sock/:/var/run/docker.sock eads-demo-pumba-kill:latest
