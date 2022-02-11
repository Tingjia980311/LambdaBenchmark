FROM public.ecr.aws/lambda/python:3.6

# Install OS packages for Pillow-SIMD
RUN yum -y install tar gzip zlib freetype-devel \
    gcc \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
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
COPY dynamicHTML.py ./

# Download ResNet50 and store it in a directory
RUN mkdir templates
COPY templates/template.html ./templates/template.html
# Set the CMD to your handler
CMD ["dynamicHTML.lambda_handler"]
