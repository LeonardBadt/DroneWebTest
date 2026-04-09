from django.db import models

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=200)
    gif_file = models.FileField(upload_to='gifs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']