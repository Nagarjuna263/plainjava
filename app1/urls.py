from django.urls import path
from app1.views import *
app_name='nag'
urlpatterns = [
    path('plainjava/',plainjava,name='plainjava'),
]
