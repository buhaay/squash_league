from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SportCenter, MyUser, Reservation

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):  # https://www.djangosnippets.org/snippets/1202/
    input_type = 'time'


class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'skill')


class CreateReservationForm(forms.ModelForm):
    time_start = forms.ChoiceField((x, str(x) + ':00') for x in range(10, 24))
    time_end = forms.ChoiceField((x, str(x) + ':00') for x in range(10, 24))
    class Meta:
        model = Reservation
        fields = ['date', 'location']
        widgets = {'date': DateInput()}
