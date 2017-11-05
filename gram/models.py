from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to='images/'+str(author))
    def __str__(self):
        return self.title