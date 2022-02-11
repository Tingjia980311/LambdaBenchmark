import json
import boto3
import numpy as np
import PIL.Image as Image

import tensorflow as tf
import tensorflow_hub as hub

IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224

IMAGE_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT)
model = tf.keras.Sequential([hub.KerasLayer("model/")])
model.build([None, IMAGE_WIDTH, IMAGE_HEIGHT, 3])

imagenet_labels= np.array(open('model/ImageNetLabels.txt').read().splitlines())

def lambda_handler(event, context):
#   bucket_name = event['Records'][0]['s3']['bucket']['name']
#   key = event['Records'][0]['s3']['object']['key']

  img = Image.open("./model/grace_hopper.jpg").resize(IMAGE_SHAPE)
  img = np.array(img)/255.0

  prediction = model.predict(img[np.newaxis, ...])
  predicted_class = imagenet_labels[np.argmax(prediction[0], axis=-1)]

  print('ImageName: {0}, Prediction: {1}'.format("grace_hopper", predicted_class))
