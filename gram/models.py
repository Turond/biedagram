from django.db import models
from django.utils import timezone
# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.title

class Follows(models.Model):
    following = models.ForeignKey('auth.User', related_name='following')
    followed_by = models.ForeignKey('auth.User', related_name='followed_by')

    def __int__(self):
        return self.following
