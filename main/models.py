from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

# exibited art pieces
class ExibitedManager(models.Manager):
    def get_queryset(self):
        return super(ExibitedManager,
                    self).get_queryset().filter(status='exibited')

# latest artpieces
class LatestPiecesManager(models.Manager):
    def get_queryset(self):
        return super(LatestPiecesManager,
                    self).get_queryset().filter(status='created')

class SaiArts(models.Model):

    STATUS_CHOICES = (
        ('created', 'Created'),
        ('exibited','Exibited')
    )
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=name)
    upload = models.ImageField(upload_to='media/', null=True, blank=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='created')
    body = models.TextField()

    class Meta:
        ordering = ('-timestamp',)
    
    def __str__(self):
        return self.name

    objects = models.Manager()

    exibited = ExibitedManager()

    created = LatestPiecesManager()

    def get_absolute_url(self):
        return reverse('main:artDetail',
         args=[self.slug])

    