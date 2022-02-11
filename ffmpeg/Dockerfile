FROM public.ecr.aws/lambda/python:3.6

# Install OS packages for Pillow-SIMD
RUN yum -y install tar gzip zlib freetype-devel \
    gcc \
    make \
    sudo \
    wget \
    && yum clean all
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
RUN tar -xvf ffmpeg-release-amd64-static.tar.xz
RUN rm ffmpeg-release-amd64-static.tar.xz
# Copy the earlier created app.py file to the container
COPY ffmpeg_lambda.py ./
COPY cut.mp4 ./
# Set the CMD to your handler
CMD ["ffmpeg_lambda.lambda_handler"]

# http://ga.video.cdn.pbs.org/videos/wfyi-local-productions/2e9d36ba-d5f6-4d45-84df-b5ca5acd551c/250267/hd-mezzanine-16x9/2c382920_l-00004055-16x9-mp4-2500k.mp4