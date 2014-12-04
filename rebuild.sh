#!/bin/bash
sudo docker stop engtv
sudo docker rm engtv
sudo docker build -t closet:5000/engtv .
sudo docker run -d -p 8080:8080 --name="engtv" closet:5000/engtv
sudo docker logs -f engtv
