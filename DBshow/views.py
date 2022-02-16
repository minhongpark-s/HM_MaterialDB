from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import DB, Rent
from .forms import rentForm
from django.utils import timezone

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

'''
def basket(request):
    return render(
        request,
        'DBshow/basket.html',
    )
'''
'''
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
            'r' : rent,
        }
    )
    '''

def testing(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/testing.html',
        {
            'db': db,
            'n': num,
            'r': rent,
        }
    )

def change_rentable_num(request, rent_id):
    db = get_object_or_404(DB, pk=rent_id)
    if request.method == "POST":
        form = rentForm(request.POST)
        if form.is_valid():
            db_ = form.save(commit=False)
            db.modifiedTime = timezone.now()
            db.rentable_num = db.rentable_num - db_.rentable_num
            db.save()
            #db_new = DB.objects.all()
            #num = DB.objects.count()
            '''
            return render(
                request,
                'DBshow/testing.html',
                {
                    'db': db_new,
                    'n': num,
                }
            )
            '''
            #return HttpResponseRedirect(reverse('127.0.0.1:8000/db/testing/'), request)
            return redirect('/db/testing/')
    else:
        form = rentForm()
        db = DB.objects.all()
        db_spec = get_object_or_404(DB, pk=rent_id)
        context = {'form': form,
                   'db': db,
                   'db_spec': db_spec,
                   }
        return render(request,
                      'DBshow/rent_form.html',
                      context)