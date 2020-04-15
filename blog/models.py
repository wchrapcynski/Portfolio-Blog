from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title
