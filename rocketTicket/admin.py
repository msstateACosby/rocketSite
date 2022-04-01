from django.contrib import admin
from .models import Ticket, TicketAdmin
# Register your models here.
admin.site.register(Ticket, TicketAdmin)