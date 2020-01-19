#!/bin/bash
docker build -t mancala .
docker run -v /home/crowley/py-mancala:/opt/project -p 8180:8180 -it mancala jupyter notebook --ip=0.0.0.0 --port=8180 --allow-root
