from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Fly, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        "flys": Fly.objects.all()
    }
    return render(request, "fly/index.html", context)

def fly(request, fly_id):
    try:
        fly = Fly.objects.get(pk=fly_id)
    except Fly.DoesNotExist:
        raise Http404("Fly Does not exist.")
    context = {
        "fly" : fly,
        "passengers": fly.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flys=fly).all()
    }
    return render(request, "fly/fly.html", context)

def book(request, fly_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        fly = Fly.objects.get(pk=fly_id)
    except KeyError:
        return render(request, "fly/error.html", {"message": "No Selection."})
        # no passenger data
    except Fly.DoesNotExist:
        return render(request, "fly/error.html", {"message": "No flys"})
    except Passenger.DoesNotExist:
        return render(request, "fly/error.html", {"message": "No passengers."})

    passenger.flys.add(fly)
    return HttpResponseRedirect(reverse("fly", args=(fly_id,)))
