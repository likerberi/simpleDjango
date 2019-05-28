from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:fly_id>", views.fly, name="fly"),
    path("<int:fly_id>/book", views.book, name="book"),
]
