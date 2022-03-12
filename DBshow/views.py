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

@login_required(login_url='common:login')
@allowed_users(allowed_roles=['하이멕 관리부원', '하이멕 일반부원'])
def Database(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/Database.html',
        {
            'db': db,
            'n': num,
            'r': rent,
        }
    )


@login_required(login_url='common:login')
def my_page(request):
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
                'DBshow/Database.html',
                {
                    'db': db_new,
                    'n': num,
                }
            )
            '''
            #return HttpResponseRedirect(reverse('127.0.0.1:8000/db/Database/'), request)
            return redirect('/Database/')
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
            dbs = DB.objects.get(product_name=rent.product_name)
            dbs.rentable_num = dbs.rentable_num + rent_.rent_num
            dbs.modifiedTime = timezone.now()
            dbs.save()


            #db_new = DB.objects.all()
            #num = DB.objects.count()
            '''
            return render(
                request,
                'DBshow/Database.html',
                {
                    'db': db_new,
                    'n': num,
                }
            )
            '''
            #return HttpResponseRedirect(reverse('127.0.0.1:8000/db/Database/'), request)
            return redirect('/my_page/')
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
def main(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    return render(
        request,
        'DBshow/main.html',
        {
            'db': db,
            'n': num,
            'r': rent,
        }
    )