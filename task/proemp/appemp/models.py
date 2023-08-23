from django.db import models

# Create your models here.
class db(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)
    position=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'