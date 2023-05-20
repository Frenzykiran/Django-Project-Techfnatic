from django.db import models
from django.core.validators import FileExtensionValidator

class Company(models.Model):
    c_name = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Background_img(models.Model):
    Back_img = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['jpg','png'])])

    def __str__(self):
        return str(self.id)

class intro_img(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['jpg','png'])])

    def __str__(self):
        return str(self.id)
    
class product1(models.Model):
    image_p1 = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return str(self.id)

class product2(models.Model):
    image_p2 = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self):
        return str(self.id)
    
class product3(models.Model):
    image_p3 = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self):
        return str(self.id)
    
class Aboutus(models.Model):
    about_us = models.ImageField(upload_to='images/', blank=True, null=True, validators=[FileExtensionValidator(['jpg','png'])])

    def __str__(self):
        return str(self.id)
    
class FacebookLink(models.Model):
    
    flink = models.CharField(max_length=100)

    def __str__(self):
        return self.flink
    
class LinkedinLink(models.Model):
    
    Llink = models.CharField(max_length=100)

    def __str__(self):
        return self.Llink