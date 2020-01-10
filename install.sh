#!/bin/bash

pip install --upgrade pip

apt-get update
apt-get install gdal-bin python-gdal python3-gdal -y
pip install GDAL

pip install matplotlib
pip install scipy==1.2.0
pip install Pillow
pip install imageio
