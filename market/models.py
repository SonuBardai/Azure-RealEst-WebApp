from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
import os

class Properties(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    slug = models.SlugField(blank=True, max_length=50)
    
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

    def __str__(self):
        return f"<{self.title}, {self.listed_by}, {self.price}>"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('market-dashboard')