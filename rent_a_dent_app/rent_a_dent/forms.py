from django import forms
from rent_a_dent.models import Visit, VISIT_TYPE
import re
from phone_field import PhoneFormField

from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = "__all__"
        labels = {'day': 'Data wizyty: ',
                  'hour': 'Godzina: ',
                  'first_name': 'Imię: ',
                  'last_name': 'Nazwisko: ',
                  'mail': 'Mail: ',
                  'phone': 'Numer telefonu: ',
                  'type': 'Typ wizyty: '
                   }
        widgets = {'day': DateInput(format='%d-%m-%Y'),
                   'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Podaj imię'}),
                   'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Podaj nazwisko'}),
                   'mail': forms.TextInput(attrs={'class': 'input', 'placeholder': 'twój@mail.pl'}),
                   'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'format: +99999999999'}),
                   'type': forms.Select(choices=VISIT_TYPE)
                   }


# class VisitPerDayForm(forms.ModelForm):
#     class Meta:
#         model = Visit
#         fields = ['day']
#         widgets = {'day': DateInput()}
