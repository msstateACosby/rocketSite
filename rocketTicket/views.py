from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse

from .models import Ticket


#create a tree like [{"head" : gemini, "children" : [{"head" : payload, "children" : [...]}]}]



def index(request):
    tickets=[]
    connectionList = []
    for ticket in Ticket.objects.filter(parentTicket=None):
        tickets.append(ticket.addNodeToTree(connectionList))



    context = {'title': "RocketTicket",'Tickets' : tickets, 'ConnectionList' : connectionList}
    parentTickets = Ticket.objects.filter(parentTicket=None)
    return render(request, 'rocketTicket/index.html', context)

