from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from django.utils.text import slugify


class Topic(models.Model):

    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True, default='static/images/mts.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def slug_title(self):
        return slugify(self.title)
