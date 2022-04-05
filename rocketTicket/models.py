from datetime import date, datetime, timedelta
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib import admin
from sympy import false, true

# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    longDescription = models.TextField()
    shortDescription = models.CharField(max_length=200)
    creationDate = models.DateField()

    urlName = models.SlugField()
    dueDate = models.DateField(null=True)

    
    parentTicket = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parent')

    #yeah these related names are dumb, but they work
    dependencies = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="dependence")
    
    children = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="childs")
    
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

    def getWarningState(self):
        returnText = "neutral"
        if (datetime.now().date() > self.dueDate):
            returnText="bad"
        elif (datetime.now().date() + timedelta(weeks=2) > self.dueDate):
            returnText="mediocre"
        if (self.isComplete):
            returnText = "good"
        return returnText

    def addNodeToTree(self, connectionList: list):
        nodeDict = {
            "title" : self.name, 
            "shortDescription": self.shortDescription, 
            "dueDate": self.dueDate.strftime("%m/%d/%Y"),
            "warningState" : self.getWarningState(),
            "slug" : self.urlName,
            "children": []
        }
        for child in self.children.all():
            nodeDict["children"].append(child.addNodeToTree(connectionList))
            connectionList.append((self.urlName, child.urlName))
        return nodeDict

    
class TicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {"urlName": ("name", )}
