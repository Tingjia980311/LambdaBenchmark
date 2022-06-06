FROM public.ecr.aws/lambda/python:3.6


RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install --upgrade setuptools

# Install the python requirements from requirements.txt
RUN python3.6 -m pip install jinja2==2.10.3

COPY dynamicHTML.py ./

# Download ResNet50 and store it in a directory
RUN mkdir templates
COPY templates/template.html ./templates/template.html
# Set the CMD to your handler
CMD ["dynamicHTML.lambda_handler"]
