FROM public.ecr.aws/lambda/python:3.6

# Copy the earlier created requirements.txt file to the container
COPY requirements.txt ./

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

# Install the python requirements from requirements.txt
RUN python3.6 -m pip install -r requirements.txt
# Replace Pillow with Pillow-SIMD to take advantage of AVX2

# Copy the earlier created app.py file to the container
# COPY synthetic-blobs-100-X-train-10000x5000.npy ./
COPY logistic.py ./
# Set the CMD to your handler
CMD ["logistic.lambda_handler"]
