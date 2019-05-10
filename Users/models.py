from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

