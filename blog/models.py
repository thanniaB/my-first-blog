from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe 

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnailClass = models.CharField(max_length=1)
    thumbnail = models.CharField(max_length=200) #todo: update this to a real image upload
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null=True)

    def display_my_safefield(self):
        return mark_safe(self.text)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
