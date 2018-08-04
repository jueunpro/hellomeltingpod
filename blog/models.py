from django.db import models

# Create your models here.

class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to="blog/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()