from django.shortcuts import render, get_object_or_404, redirect
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
            'r' : rent,
        }
    )

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


def changeDBandRefreshPage(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        data = {'id': id, 'name': name}

        return render(request, 'DBshow/testing.html', data)

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