from django.urls import path
from fps.views.rooms.index import get_room_list,build_room,remove_room

urlpatterns = [
    path('get_room_list/',get_room_list),
    path('build_room/',build_room),
    path('remove_room/',remove_room),
]
