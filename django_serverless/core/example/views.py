from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, parsers
from .models import DropBox
from .serializers import DropBoxSerializer
from .forms import UploadFileForm
import json
import boto3
import uuid
import string
import random
import time

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DropBoxViewset(viewsets.ModelViewSet):

    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_namserializer_classes = ['get', 'post', 'patch', 'delete']


def submit_size(request):
    return render(request, 'search_form.html', {'hello': 'Hello World'})

def generate_file(request):  
    request.encoding='utf-8'
    size = int(request.GET['q'])
    random_str = '1' * size
    # all_chars = string.ascii_letters + string.digits + string.punctuation
    # with open("/tmp/output.json", "w") as output:
    #     json.dumps(random_str, output)
    s3 = boto3.resource('s3')
    # random_str = ''.join(random.choices(all_chars, k=size))
    filename = str(size) + ".txt"
    object = s3.Object('newdbctj', filename)
    object.put(ACL='public-read', Body = random_str, Key = filename)


    return HttpResponse("generate a " + str(size) + " file and upload it to s3")


def upload_file(request):
    receive_t = time.time()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = str(uuid.uuid4()) + '.txt'
            with open('/tmp/' + file_name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            save_t = time.time()
            s3 = boto3.resource('s3')
            # s3.upload_file('/tmp/' + file_name, 'newdbctj', file)
            s3.Bucket('newdbctj').upload_file('/tmp/' + file_name,file_name)
            upload_t = time.time()
            save_time = save_t - receive_t
            upload_time = upload_t - save_t
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponse("upload file to s3, " + "save_time: " + str(save_time) + " upload_time: " + str(upload_time))
    else:
        form = UploadFileForm()
        return render(request, 'upload_form.html', {
                'form': form
        })