from django import forms
from DBshow.models import DB, Rent


class rentForm(forms.ModelForm):
    class Meta:
        model = DB
        fields = ['rentable_num']
        labels = {
            'rentable_num': 'content',
        }
