from django.db import models

# Create your models here.

class Demo(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.TextField()



