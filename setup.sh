#!/bin/bash

# Atualizar conda e instalar Python 3.12.2
conda update -n base -c defaults conda -y
conda install -y python=3.12.2

# Instalar g++ (Ubuntu 13.2.0)
apt-get update && apt-get install -y g++ && apt-get clean

# Configurar pastas para extensões do VS Code
mkdir -p /root/.vscode-server/extensions
mkdir -p /root/.vscode-server/data/Machine
