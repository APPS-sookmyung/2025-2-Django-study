from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    url = models.URLField
    email = models.EmailField()
    creat = models.DateTimeField(auto_now_add=True)


