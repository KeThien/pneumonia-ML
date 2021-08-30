from django.db import models
from django.utils import timezone
# Create your models here.


class Image(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True)
    result = models.FloatField(null=True, blank=True)
