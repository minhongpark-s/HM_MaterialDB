from django import forms
from DBshow.models import DB, Rent, LCdata


class rentForm(forms.ModelForm):
    class Meta:
        model = DB
        fields = ['rentable_num']
        labels = {
            'rentable_num': 'content',
        }

class returnForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['rent_num']
        labels = {
            'rent_num': 'content',
        }

class LCForm(forms.ModelForm):
    class Meta:
        model = LCdata
        fields = ['LC_rent_name',
                  'LC_phone_number',
                  'LC_purpose',
                  'LC_availTime',
                  'LC_thickness',
                  'LC_width',
                  'LC_height',
                  'LC_who']


