from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class SaiArts(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=name)
    upload = models.ImageField(upload_to='media/', null=True, blank=True)
    body = models.TextField()

    class Meta:
        ordering = ('-timestamp',)
    
    def __str__(self):
        return self.name

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('main:artDetail',
         args=[self.slug])

    