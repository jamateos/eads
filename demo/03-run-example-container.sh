#!/bin/bash
docker run -d --name examplevotingapp_app dockersamples/examplevotingapp_vote:latest; 
watch -d docker ps

