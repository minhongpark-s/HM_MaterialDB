from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import DB, Rent
from .forms import rentForm, returnForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from common.decorators import allowed_users
from django.db.models import Q

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
@allowed_users(allowed_roles=['하이멕 관리부원', '하이멕 일반부원'])
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
            rent = Rent(name=request.user,
                        product_name=db.product_name,
                        rent_num=db_.rentable_num,
                        rent_date=timezone.now()
                        )
            rent.save()
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


@login_required(login_url='common:login')
def change_rent_num(request, rent_id):
    rent = get_object_or_404(Rent, pk=rent_id)
    if request.method == "POST":
        form = returnForm(request.POST)
        if form.is_valid():
            rent_ = form.save(commit=False)
            rent.rent_num = rent.rent_num - rent_.rent_num
            rent.save()
            dbs = DB.objects.filter(Q(product_name=rent_.product_name))
            forms = rentForm(dbs)
            dbs_ = forms.save(commit=False)
            dbs_.rentable_num = dbs_.rentable_num + rent_.rent_num
            dbs_.modifiedTime = timezone.now()
            dbs_.save()


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
        form = returnForm()
        db = DB.objects.all()
        rent = Rent.objects.all()
        rent_spec = get_object_or_404(Rent, pk=rent_id)
        context = {'form': form,
                   'db': db,
                   'rent_spec': rent_spec,
                   'rent': rent,
                   }
        return render(request,
                      'DBshow/return_form.html',
                      context)

@login_required(login_url='common:login')
def newpagetesting(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/newpagetesting.html',
        {
            'db': db,
            'n': num,
            'r': rent,
        }
    )