import os.path
import uuid
from django.db import models

def unique_image_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    # full_name = "%s.%s" % (name, ext)
    return os.path.join('employees', full_name)

class Employees(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    social_fb = models.CharField(max_length=100)
    social_tweet = models.CharField(max_length=100)
    social_ig = models.CharField(max_length=100)
    profile = models.ImageField(upload_to=unique_image_name, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Offers(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=unique_image_name, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    guests_number = models.IntegerField()
    date = models.DateField(null=False, blank=False)
    time = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

