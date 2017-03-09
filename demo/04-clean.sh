#!/bin/bash
docker ps --all | grep eads-demo-pumba-kill | awk '{print $1}' | xargs docker rm
docker ps --all | grep examplevotingapp_vote | awk '{print $1}' | xargs docker rm
docker images | grep eads-demo-pumba-kill | awk '{print $3}' | xargs docker rmi
docker ps | grep gaiadocker/tugbot | awk '{print $1}' | xargs docker stop
docker ps --all | grep gaiadocker/tugbot | awk '{print $1}' | xargs docker rm

