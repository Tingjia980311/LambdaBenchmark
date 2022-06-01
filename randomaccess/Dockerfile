FROM public.ecr.aws/lambda/python:3.6

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

RUN python3.6 -m pip install numpy

COPY input.dat ./
COPY randomaccess.py ./
# Set the CMD to your handler
CMD ["randomaccess.lambda_handler"]
