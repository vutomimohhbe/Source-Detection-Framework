#!/bin/bash
pip install -r requirements.txt
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..
echo "Dependencies installed!"
