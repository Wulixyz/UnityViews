from django.urls import path,include
from fps.views.index import index

urlpatterns = [
    path("",index),
    path("rooms/",include("fps.urls.rooms.index")),
    path("gameusers/",include("fps.urls.gameusers.index")),
]
