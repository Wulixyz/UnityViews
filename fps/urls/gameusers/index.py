from django.urls import path
from fps.views.gameusers.login import login
from fps.views.gameusers.register import register
from fps.views.gameusers.remove_user import remove_user

urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('remove_user/',remove_user),
]
