from django.urls import path,include
from fps.views.schedule.index import index

urlpatterns = [
    path('',index),
]
