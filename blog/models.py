from django.db import models
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    classes = models.TextField(help_text="Enter the classes separated by commas", default="Add Classes Here")
    available_hours = models.TextField(help_text="Enter available hours", default="Not Specified")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})