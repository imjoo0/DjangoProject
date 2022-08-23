from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10,null = True)
    content = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)