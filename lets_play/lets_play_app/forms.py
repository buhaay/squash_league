from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SportCenter, MyUser, Reservation
from .widgets import SelectTimeWidget

class DateInput(forms.DateInput):
   input_type = 'date'


class TimeInput(forms.TimeInput):  # https://www.djangosnippets.org/snippets/1202/
   input_type = 'time'


class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'skill')


class CreateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time_start', 'time_end', 'location']
        widgets = {'date': DateInput(),
                   'time_start': TimeInput(),
                   'time_end': TimeInput(),
                   }
