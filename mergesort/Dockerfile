FROM public.ecr.aws/lambda/python:3.6

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

RUN python3.6 -m pip install numpy

COPY mergesort.py ./
# Set the CMD to your handler
CMD ["mergesort.lambda_handler"]
