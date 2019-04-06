from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=35)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
