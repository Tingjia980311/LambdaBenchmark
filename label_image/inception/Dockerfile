# Pull the base image with python 3.8 as a runtime for your Lambda
FROM public.ecr.aws/lambda/python:3.6

# Copy the earlier created requirements.txt file to the container
COPY requirements.txt ./

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

# Install the python requirements from requirements.txt
RUN python3.6 -m pip install -r requirements.txt

# Copy the earlier created app.py file to the container
COPY inception.py ./

# Download ResNet50 and store it in a directory
RUN mkdir model

RUN curl -L "https://storage.googleapis.com/download.tensorflow.org/models/inception_v3_2016_08_28_frozen.pb.tar.gz" -o ./model/inception_v3_2016_08_28_frozen.pb.tar.gz
RUN tar -xf model/inception_v3_2016_08_28_frozen.pb.tar.gz -C model/
RUN chmod 644 model/inception_v3_2016_08_28_frozen.pb
RUN chmod 755 model/inception_v3_2016_08_28_frozen.pb
RUN chmod 644 model/imagenet_slim_labels.txt
RUN chmod 755 model/imagenet_slim_labels.txt
# download resnet
# RUN curl -L https://tfhub.dev/google/imagenet/resnet_v1_50/classification/4?tf-hub-format=compressed -o ./model/resnet.tar.gz
# RUN tar -xf model/resnet.tar.gz -C model/
RUN curl -L https://github.com/second-state/AI-as-a-Service/raw/master/native_model_zoo/image_classification_mobilenet_v2_14_224/src/mobilenet_v2_1.4_224_frozen.pb -o ./model/mobilenet_v2_1.4_224_frozen.pb

RUN rm -r model/inception_v3_2016_08_28_frozen.pb.tar.gz
RUN curl -L https://github.com/tensorflow/tensorflow/raw/r1.15/tensorflow/examples/label_image/data/grace_hopper.jpg -o ./model/grace_hopper.jpg

# Set the CMD to your handler
CMD ["inception.lambda_handler"]