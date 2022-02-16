from django.shortcuts import render, get_object_or_404, redirect
from .models import DB, Rent
from .forms import rentForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from common.decorators import allowed_users

# Create your views here.

@login_required(login_url='common:login')
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
@login_required(login_url='common:login')
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


@login_required(login_url='common:login')
def mypage(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    num_r = Rent.objects.count()
    return render(
        request,
        'DBshow/mypage.html',
        {
            'db': db,
            'n': num,
            'r': rent,
            'nr': num_r,
        }
    )


@login_required(login_url='common:login')
def change_rentable_num(request, rent_id):
    db = get_object_or_404(DB, pk=rent_id)
    if request.method == "POST":
        form = rentForm(request.POST)
        if form.is_valid():
            db_ = form.save(commit=False)
            db.modifiedTime = timezone.now()
            db.rentable_num = db.rentable_num - db_.rentable_num
            db.save()
            db_new = DB.objects.all()
            num = DB.objects.count()
            return render(
                request,
                'DBshow/testing.html',
                {
                    'db': db_new,
                    'n': num,
                }
            )
    else:
        form = rentForm()
        context = {'form': form,
                   'db': db}
        return render(request,
                      'DBshow/rent_form.html',
                      context)