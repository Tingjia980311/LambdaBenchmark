from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf.urls import url
from . import views

router = SimpleRouter()
router.register('accounts', views.DropBoxViewset)
urlpatterns = router.urls
# urlpatterns = []
urlpatterns.append(path('', views.index, name='index'))
urlpatterns.append(path('size-form', views.submit_size, name='submit_size'))
urlpatterns.append(url(r'^generate/$', views.generate_file))
urlpatterns.append(path('upload_to_s3', views.upload_file, name='upload_file'))