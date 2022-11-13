#!/bin/bash

# Set setup file to executable
chmod +x client/setup.sh
chmod +x server/setup.sh

# Setup client and server
./client/setup.sh
./server/setup.sh