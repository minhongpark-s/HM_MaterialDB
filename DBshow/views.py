from django.shortcuts import render
from .models import DB, Rent

# Create your views here.

def index(request):
    db = DB.objects.all()
    return render(
        request,
        'DBshow/index.html',
        {
            'db': db,
        }
    )


def basket(request):
    return render(
        request,
        'DBshow/basket.html',
    )

def check(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/check.html',
        {
            'db': db,
            'n' : num,
            'rent' : Rent,
        }
    )