#!/bin/bash

# Set setup file to executable
chmod +x client/setup.sh
chmod +x server/setup.sh

export REPO_DIR=$(pwd)

# Setup client and server
$REPO_DIR/client/setup.sh
$REPO_DIR/server/setup.sh