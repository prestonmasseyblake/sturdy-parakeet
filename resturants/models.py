from django.db import models

# Resturant
class Resturant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Deal
class Deal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount_off = models.CharField(max_length=50)

    def __str__(self):
        return self.title
