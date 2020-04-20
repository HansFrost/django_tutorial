from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(null=True, max_length=100)
    desc = models.TextField(null=True)
    img = models.ImageField(null=True, upload_to="pics")
    price = models.IntegerField(null=True)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

