from django.db import models
class Images(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'static/')
    description = models.TextField()
    location = models.CharField(max_length = 100)
    type= models.CharField(max_length = 29)

class Gallery(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'static/')
    name = models.CharField(max_length = 50)
class Politics(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'static/') 
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    about_khadpu = models.TextField()  
    facebook = models.CharField(max_length = 100)
class text_info(models.Model):
    id = models.AutoField(max_length = 10 , primary_key = True)
    image = models.ImageField(upload_to='static/' , blank = True)
    name = models.CharField(max_length = 100)
    info_text = models.TextField()
# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
