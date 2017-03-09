#!/bin/bash
docker run -d --name tugbot-run -v /var/run/docker.sock:/var/run/docker.sock gaiadocker/tugbot:master
docker ps
