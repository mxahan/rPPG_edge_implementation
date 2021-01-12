#!/bin/bash
echo "Very sad life"
ffmpeg -t 22 -f v4l2 -framerate 30 -video_size 1920x1080 -c:v mjpeg -i /dev/video1 output.mov
python3 file_main.py

