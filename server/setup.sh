#!/bin/bash

echo "========== Server setup =========="

cd $REPO_DIR/server

echo "Installing python packages ..."
pip install -r requirements.txt

chmod +x resource_monitoring_server.py

cd $REPO_DIR

# Install redis server
echo "Download redis ..."
curl -o redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
tar -xzf redis-stable.tar.gz
mv redis-stable redis -f
rm redis-stable.tar.gz

echo "Build redis ..."
cd $REPO_DIR/redis
make -j${nproc} > /dev/null 2>&1
echo "Done"
