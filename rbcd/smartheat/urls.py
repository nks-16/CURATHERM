# smartheat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/upload-image', views.upload_image, name='upload_image'),
    path('analysis/', views.analysis, name='analysis'),
    path('about/', views.about, name='about'),
]
