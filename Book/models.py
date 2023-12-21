from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isdeleted = models.BooleanField(default=False)
    price = models.IntegerField()
             

    def __str__(self):
        return f"{self.title}"
    

    class Meta:
        db_table = "Book"
