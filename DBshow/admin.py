from django.contrib import admin
from .models import DB
from .models import Rent, LCdata
# Register your models here.

admin.site.register(DB)
admin.site.register(Rent)
admin.site.register(LCdata)