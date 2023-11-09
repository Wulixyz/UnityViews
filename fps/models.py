from django.db import models

class Room(models.Model):
    name = models.CharField(default="Room",max_length=100)
    port = models.IntegerField(default=7777)

    def __str__(self):
        return self.name + ' - ' + str(self.port)

class GameUsers(models.Model):
    username = models.CharField(default="yyd",max_length=20)
    password = models.CharField(default="",max_length=30)

    def __str__(self):
        return self.username
