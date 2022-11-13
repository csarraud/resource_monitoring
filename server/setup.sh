#!/bin/bash

echo "========== Server setup =========="

# Install redis server
echo "Download redis ..."
curl -o redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
tar -xzf redis-stable.tar.gz
mv redis-stable redis
rm redis-stable.tar.gz

echo "Build redis ..."
cd redis
make -j${nproc} > /dev/null 2>&1
echo "Done"
