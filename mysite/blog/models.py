from django.db import models
from django.utils import timezone
from django.urls import reverse
#from django.core.urlresolvers import reverse



# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Posting(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    title = models.CharField(max_length=128)
    text = models.TextField(default='NO CONTENT')
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
