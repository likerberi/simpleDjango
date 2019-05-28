from django.contrib import admin
from .models import Airport, Fly, Passenger

class PassengerInline(admin.StackedInline):
    model = Passenger.flys.through 
    extra = 1

class FlyAdmin(admin.ModelAdmin):
    #list_display = ('',)
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    #list_display = ('',)
    #django admin, -> & <- delete & add property
    filter_horizontal = ("flys",)


admin.site.register(Airport)
admin.site.register(Fly, FlyAdmin)
admin.site.register(Passenger, PassengerAdmin)

# Register your models here.
