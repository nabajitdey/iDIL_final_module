from django.db import models

class Hotel(models.Model):
    name= models.CharField(max_length=50, unique= True)
    class Meta:
        ordering = ['name']


class Image(models.Model):
    image = models.ImageField(upload_to='images/', default=None)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,default=1)


class Object(models.Model):
    name= models.CharField(max_length=50, unique= True)
    images = models.ManyToManyField(Image)
    hotels = models.ManyToManyField(Hotel)

    class Meta:
        ordering = ['name']

class Group(models.Model):
    name = models.CharField(max_length=50, unique= True)
    object_name = models.ManyToManyField(Object)

    class Meta:
        ordering = ['name']