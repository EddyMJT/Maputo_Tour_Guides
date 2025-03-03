from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify


class Tour(models.Model):

    title = models.CharField(max_length=200)
    short_description = QuillField(blank=True, null=True)
    full_description = QuillField(blank= True, null=True)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True, default='/static/images/mts.jpg')
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    home_page = models.CharField(max_length=100)
    duration = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    participants_ages = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    pick_up_location = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    included = QuillField(blank=True, null=True)
    expected = QuillField(blank=True, null=True)
    accessibility = models.CharField(max_length=100)
    additional_info = QuillField(blank=True, null=True)
    cancellation_policy = QuillField(blank=True, null=True)
    FAQ = QuillField(blank=True, null=True)
    image_2 = models.ImageField(upload_to='media/images/', null=True, blank=True, default='/static/images/mts.jpg')
    image_3 = models.ImageField(upload_to='media/images/', null=True, blank=True, default='/static/images/mts.jpg')

    def __str__(self):
        return self.title

    @property
    def slug_title(self):
        return slugify(self.title)


class Photo(models.Model):

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/', null=False, blank=False)

    def __str__(self):
        return self.image