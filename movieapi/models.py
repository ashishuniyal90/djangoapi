from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=256)
	laguage = models.CharField(max_length=256)
	actor = models.CharField(max_length=256)

	def __str__(self):
		return self.name