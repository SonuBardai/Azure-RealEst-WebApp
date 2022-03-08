from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Properties(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    listing_date = models.DateTimeField(default = timezone.now)
    price = models.IntegerField()
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=50)    # name of img stored in filesystem

    def __str__(self):
        return f"<{self.title}, {self.listed_by}, {self.price}>"