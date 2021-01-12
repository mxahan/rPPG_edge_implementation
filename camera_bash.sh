
#!/bin/bash
echo "Hello World!"

# video input


ffmpeg -t 20 -f v4l2 -framerate 90 -video_size 1280x720 -input_format mjpeg -i /dev/video0 output.mov
python file_main.py
