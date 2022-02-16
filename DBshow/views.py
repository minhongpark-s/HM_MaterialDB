from django.shortcuts import render
from .models import DB, Rent

# Create your views here.

def index(request):
    db = DB.objects.all()
    return render(
        request,
        'DBshow/templates/DBshow/index.html',
        {
            'db': db,
        }
    )


def basket(request):
    return render(
        request,
        'DBshow/templates/DBshow/basket.html',
    )

def check(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/templates/DBshow/check.html',
        {
            'db': db,
            'n' : num,
            'r' : rent,
        }
    )

def testing(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/templates/DBshow/testing.html',
        {
            'db': db,
            'n': num,
            'r': rent,
        }
    )