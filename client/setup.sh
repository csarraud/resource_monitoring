#!/bin/bash
echo "========== Client setup =========="

cd $REPO_DIR/client

echo "Installing python packages ..."
pip install -r requirements.txt

chmod +x resource_monitoring_client.py