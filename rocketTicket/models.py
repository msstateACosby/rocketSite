from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib import admin
from sympy import true

# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    longName = models.TextField()
    shortName = models.CharField(max_length=200)
    creationDate = models.DateField()

    urlName = models.SlugField()
    dueDate = models.DateField(null=True)
    parentTicket = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    dependencies = models.ManyToManyField('self')
    
    isComplete = models.BooleanField(default=False)

    class TicketAdmin(admin.ModelAdmin):
        prepopulated_fields = {"urlName": ("name", )}