#!/bin/bash
echo "========== Client setup =========="

cd client

echo "Installing python packages ..."
pip install -r requirements.txt

chmod +x resource_monitoring_client.py