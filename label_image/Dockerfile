FROM public.ecr.aws/lambda/python:3.6

# Install OS packages for Pillow-SIMD
RUN yum -y install tar gzip zlib freetype-devel \
    gcc \
    ghostscript \
    lcms2-devel \
    libffi-devel \
    libimagequant-devel \
    libjpeg-devel \
    libraqm-devel \
    libtiff-devel \
    libwebp-devel \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
    tcl-devel \
    tk-devel \
    tkinter \
    which \
    xorg-x11-server-Xvfb \
    zlib-devel \
    && yum clean all

# Copy the earlier created requirements.txt file to the container
COPY requirements.txt ./

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

# Install the python requirements from requirements.txt
RUN python3.6 -m pip install -r requirements.txt
# Replace Pillow with Pillow-SIMD to take advantage of AVX2

# Copy the earlier created app.py file to the container
COPY label_image.py ./

# Download ResNet50 and store it in a directory
RUN mkdir model
RUN curl -L https://github.com/second-state/AI-as-a-Service/raw/master/native_model_zoo/image_classification_mobilenet_v2_14_224/src/mobilenet_v2_1.4_224_frozen.pb -o ./model/mobilenet_v2_1.4_224_frozen.pb

# Download ImageNet labels
RUN curl https://raw.githubusercontent.com/emgucv/models/master/inception_v3_slim/imagenet_slim_labels.txt -o ./model/imagenet_slim_labels.txt

RUN curl -L https://github.com/tensorflow/tensorflow/raw/r1.15/tensorflow/examples/label_image/data/grace_hopper.jpg -o ./model/grace_hopper.jpg
# Set the CMD to your handler
CMD ["label_image.lambda_handler"]
