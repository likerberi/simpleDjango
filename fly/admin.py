from django.contrib import admin
from .models import Airport, Fly, Passenger

admin.site.register(Airport)
admin.site.register(Fly)
admin.site.register(Passenger)

# Register your models here.
