from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse

from .models import Ticket

# Create your views here.
def index(request):

    context = {'Title': "RocketTicket",'Tickets' : []}
    parentTickets = Ticket.objects.filter(parentTicket=None)
    return render(request, 'rocktTicket/index.html', context)

