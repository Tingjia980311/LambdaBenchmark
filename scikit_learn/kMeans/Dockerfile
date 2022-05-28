FROM public.ecr.aws/lambda/python:3.6


RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

# Install the python requirements of scikit-learn
RUN python3.6 -m pip install scikit-learn

# Copy the earlier created app.py file to the container
COPY kMeans.py ./
# Set the CMD to your handler
CMD ["kMeans.lambda_handler"]
