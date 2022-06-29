from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=700)
    description = models.CharField(max_length=200)
    price = models.IntegerField()


def __str__(self):
    return f"name:{self.name}: description {self.description}"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



def __str__(self):
    return f"name:{self.name}: email {self.email}"
