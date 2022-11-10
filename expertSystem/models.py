from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id) + '-' + self.label

class Option(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return str(self.id) + '-' + self.label

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    response = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    options = models.ManyToManyField(Option, related_name='cars')

    def __str__(self):
        return str(self.id) + '-' + self.response