from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import DB, Rent, LCdata
from .forms import rentForm, returnForm, LCForm
from django.utils import timezone
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from common.decorators import allowed_users
from django.db.models import Q
import pandas as pd
import warnings

@login_required(login_url='common:login')
def LC(request):
    return render(
        request,
        'DBshow/LC_form.html'
    )

@login_required(login_url='common:login')
def LC_reserve(request):
    if request.method == "POST":
        '''
        return render(
            request,
            'DBshow/LC_form.html',
        )
        '''
        form = LCForm(request.POST)
        '''
        return render(
            request,
            'DBshow/LC_form.html',
            {
                'form':form,
            }
        )
        '''
        if form.is_valid():
            form_ = form.save(commit=False)
            '''
            return render(
                request,
                'DBshow/LC_form.html',
                {
                    'form_':form_,
                }
            )
            '''
            obj = LCdata.objects.create(
                LC_rent_name=request.user.username,
                LC_phone_number=form_.LC_phone_number,
                LC_purpose=form_.LC_purpose,
                LC_availTime=form_.LC_availTime,
                LC_thickness=form_.LC_thickness,
                LC_width=form_.LC_width,
                LC_height=form_.LC_height,
                LC_who=form_.LC_who,
            )
            obj.save()
        #else:
            return redirect('/main/')

            #return HttpResponseRedirect(reverse('127.0.0.1:8000/main/'), request)
            #return redirect('/Database/')
            #return redirect('/main/')
    else:
        form = LCForm()
        context = {
            'form': form,
                   }
        return render(request,
                      'DBshow/LC_form.html',
                      context)


@login_required(login_url='common:login')
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
@allowed_users(allowed_roles=['관리자'])
def xlsxAdd(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    num_r = Rent.objects.count()

    # warnigs 메세지 삭제
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        # 엑셀 읽어오는 부분
        df = pd.read_excel(
            "/home/ubuntu/fileShare/share/excel_.xlsx", engine="openpyxl")

    # list 값이 모두 NaN인 데이터 제외
    data = df.dropna(how='all')

    # 엑셀 데이터 db insert
    for dbfram in data.itertuples():
        obj = DB.objects.create(
            product_name=dbfram.name,
            rentable_num=dbfram.number,
            total_num=dbfram.number,
            registeredTime=timezone.now(),
            modifiedTime=timezone.now(),
            tag=dbfram.tag,

        )
        obj.save()

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
@allowed_users(allowed_roles=['관리자'])
def DeleteDB(request):
    db = DB.objects.all()
    num = DB.objects.count()
    rent = Rent.objects.all()
    num_r = Rent.objects.count()

    DB.objects.all().delete()
    Rent.objects.all().delete()

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
@allowed_users(allowed_roles=['관리자','하이멕 임원진','하이멕 관리부원', '하이멕 일반부원'])
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
            db_new = DB.objects.all()
            num = DB.objects.count()
            rent = Rent.objects.all()
            num_r = Rent.objects.count()
            return render(
                request,
                'DBshow/Database.html',
                {
                    'db': db_new,
                    'n': num,
                    'r': rent,
                    'nr': num_r,
                }
            )
            #return HttpResponseRedirect(reverse('127.0.0.1:8000/db/Database/'), request)
            #return redirect('/Database/')
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
@allowed_users(allowed_roles=['관리자','하이멕 임원진','하이멕 관리부원', '하이멕 일반부원'])
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