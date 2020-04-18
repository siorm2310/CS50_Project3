from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "menu.html")


def menu(request):
    pizzas = Pizza.objects.all()
    subs = Sub.objects.all()
    other_dishes = OtherDish.objects.all()
    toppings = ToppingsAndExtras.objects.all()

    menu_items = {
        "pizzas": pizzas,
        "subs": subs,
        "other_dishes": other_dishes,
        "toppings": toppings,
    }
    return render(request, "menu.html", context=menu_items)
