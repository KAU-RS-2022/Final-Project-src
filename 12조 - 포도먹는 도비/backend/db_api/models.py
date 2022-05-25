from django.db import models

# Create your models here.
class Test(models.Model):
    dataNumber = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name