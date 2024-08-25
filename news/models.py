from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to="news/banner")
    content = models.TextField(max_length=2000)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    url = models.CharField(max_length=2000)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.url
