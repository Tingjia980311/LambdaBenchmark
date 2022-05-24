mkdir data
cd data
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xvf ffmpeg-release-amd64-static.tar.xz
./ffmpeg-5.0.1-amd64-static/ffmpeg -i video.mp4 -ss 00:00:00 -t 00:02:00 -c:v copy -c:a copy cut.mp4