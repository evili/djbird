from django.db import models

# Create your models here.
class BaseName(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        abstract = True
        ordering = ['name']

class Genus(BaseName):
    pass

class Species(BaseName):
    genus = models.ForeignKey(Genus)


