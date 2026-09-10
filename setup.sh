#!/bin/bash

set -e

echo "================================="
echo "  PI 4 Offline Computer Setup"
echo "=================================" 

echo "Updating package lists..." 
sudo apt update

echo "installing basic tools..." 
sudo apt install -y git python3 curl

echo "Setup complete" 
