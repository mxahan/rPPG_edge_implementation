
#!/bin/bash
echo "Hello World!"

# video input


ffmpeg -t 22 -f v4l2 -framerate 30 -video_size 1280x720 -input_format mjpeg -i /dev/video0 output.mov
python file_main.py
