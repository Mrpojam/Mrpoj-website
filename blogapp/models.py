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
    github = models.CharField(max_length = 200, blank = True)
    linkedin = models.URLField(blank = True)
    interests = models.TextField(max_length = 5000, blank = True)

    def __str__ (self):
        return self.name

class Experince (models.Model):
    title = models.CharField(max_length = 100)
    job = models.CharField(max_length = 100)
    memo = models.TextField(max_length = 4000)
    date = models.DateField()

    def __str__ (self):
        return self.title

class Education (models.Model):
    instutation = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 100)
    memo = models.TextField(max_length = 4000)
    link = models.URLField(blank = True)

    def __str__ (self):
        return self.instutation


class Tools (models.Model):
    titile = models.CharField(max_length = 10)
    thumbnail = models.ImageField(upload_to = 'images')
class Skills (models.Model):
    memo = models.TextField(max_length = 500)

    def __str__ (self):
        return self.memo

class Awards (models.Model):
    memo = models.TextField(max_length = 500)

    def __str__ (self):
        return self.memo
