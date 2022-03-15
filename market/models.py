from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
import os
from django.conf import settings

class Properties(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    slug = models.SlugField(blank=True, max_length=50)
    
    location = models.TextField()
    listing_date = models.DateTimeField(default = timezone.now)
    
    size = models.IntegerField(
        validators=[
            MinValueValidator(100)
        ]
    )

    bedrooms = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )

    price = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    image1 = models.ImageField(upload_to="property_pics")
    image2 = models.ImageField(blank=True, upload_to="property_pics")
    image3 = models.ImageField(blank=True, upload_to="property_pics")

    thumbnail = models.TextField(blank=True)

    def __str__(self):
        return f"<{self.title}, {self.listed_by}, {self.price}>"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # Creating a Slug for the Property

        split_name = self.image1.name.split('/')
        if len(split_name) == 2:
            new_name = 'thumbnail-' + split_name[1]
        else: 
            new_name = 'thumbnail-' + split_name[0]
        self.thumbnail = '/media/property_pics/'+new_name
        # Sets the name of the Thumbnail being set

        super().save(*args, **kwargs)
        
        path = os.path.join(settings.MEDIA_ROOT, 'property_pics', new_name)
        
        img = Image.open(self.image1.path)
        if img.height > 200 or img.width > 200:
            size = (600, 400)
            img.thumbnail(size)
            img.save(path)
        # Creating the thumbnail from the original image1 file

    
    def get_absolute_url(self):
        return reverse('market-dashboard')