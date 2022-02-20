from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to="category",blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return '{}'.format(self.name)

class District(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Place(models.Model):
    name = models.CharField(max_length=50,unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)