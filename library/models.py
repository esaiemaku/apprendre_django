from django.db import models

class Book(models.Model):

    titre=models.CharField(max_length=255)
    ISBN=models.CharField(max_length=50, unique=True) 
    auteur=models.CharField(max_length=67)
    edition=models.CharField(max_length=65)
    price=models.FloatField()
    record_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

