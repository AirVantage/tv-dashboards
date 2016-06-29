#!/bin/sh
sudo docker stop engtv
sudo docker rm engtv
sudo docker build -t airvantage/engtv .
sudo docker run -d -p 8080:8080 --name="engtv" airvantage/engtv
sudo docker logs -f engtv
