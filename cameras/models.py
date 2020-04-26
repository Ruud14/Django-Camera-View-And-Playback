from django.db import models


class Camera(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.title
