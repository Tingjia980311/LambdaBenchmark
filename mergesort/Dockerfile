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
COPY mergesort.py ./
# Set the CMD to your handler
CMD ["mergesort.lambda_handler"]
