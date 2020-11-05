from django.db import models

class Settings (models.Model):
    name = models.CharField (max_length = 50, blank = True)
    family = models.CharField (max_length = 50, blank = True)
    pic = models.ImageField (upload_to = 'images')
    about = models.TextField(max_length = 4000, blank = True)
    one_line = models.TextField(max_length = 100, blank = True)
    email = models.EmailField (blank = True)
    twitter = models.URLField(blank = True)
    instagram = models.URLField(blank = True)
    telegram = models.URLField(blank = True)
    spotify = models.URLField(blank = True)
    guthub = models.URLField(blank = True)
    linkedin = models.URLField(blank = True)
    interests = models.TextField(max_length = 5000, blank = True)

class Experince (models.Model):
    title = models.CharField(max_length = 100)
    job = models.CharField(max_length = 100)
    memo = models.TextField(max_length = 4000)
    date = models.DateField()

class Education (models.Model):
    instutation = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 100)
    memo = models.TextField(max_length = 4000)
    link = models.URLField(blank = True)

class Skills_tools (models.Model):
    Class = models.CharField(max_length = 100, blank = True)

class Skills (models.Model):
    memo = models.TextField(max_length = 500)

class Awards (models.Model):
    memo = models.TextField(max_length = 500)
