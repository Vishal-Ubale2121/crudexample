from django.db import models

class Employee(models.Model):
    car = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    prise = models.CharField(max_length=15)
    model = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',blank=True)


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    file = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return self.title