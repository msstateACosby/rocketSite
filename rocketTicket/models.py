from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib import admin
from sympy import false, true

# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    longName = models.TextField()
    shortName = models.CharField(max_length=200)
    creationDate = models.DateField()

    urlName = models.SlugField()
    dueDate = models.DateField(null=True)
    parentTicket = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parent')

    dependencies = models.ManyToManyField('self', blank=True)
    children = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    isComplete = models.BooleanField(default=False)

    previousParentTicket = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previousParentTicket = self.parentTicket
        #print(self.parentTicket)
    def __str__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):

        
        super().save(force_insert, force_update, *args, **kwargs)
        
        if (self.previousParentTicket != self.parentTicket):
            
            if (self.previousParentTicket != None):
                self.previousParentTicket.children.remove(self)
            
            if (self.parentTicket != None):
                print(self.parentTicket)
                print(self.parentTicket.children.all())
                self.parentTicket.children.add(self)
                self.parentTicket.save()
            
                print(self.parentTicket.children.all())
                
                
                self.previousParentTicket = self.parentTicket

    def addNodeToTree(self):
        nodeDict = {"title" : self.name, "children": []}
        for child in self.children.all():
            nodeDict["children"].append(child.addNodeToTree())
        return nodeDict

    
class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {"urlName": ("name", ), "shortName" : ("longName",)}
