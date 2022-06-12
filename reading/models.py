from django.db import models
#from django.db import pepito

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} is {self.pages} long'


    

