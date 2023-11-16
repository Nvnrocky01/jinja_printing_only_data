from django.urls import path
from app1.views import *
urlpatterns=[
    path('nvn/',nvn,name='nvn'),
]