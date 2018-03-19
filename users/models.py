import datetime

from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=200)

    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.username
    def was_signed_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

class NewsCategory(models.Model):
    category = models.TextField()
    def __str__(self):
        return self.category


class News(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=200)
    published = models.CharField(max_length=20)
    date =  models.DateTimeField('date published')


