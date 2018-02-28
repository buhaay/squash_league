from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SportCenter, MyUser
from lets_play_app.models import Rooms
from datetimepicker.widgets import DateTimePicker

SPORT_CENTRES = SportCenter.objects.all()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'skill')


class CreateReservationForm(forms.Form):
    location = forms.ChoiceField(choices=((center.id, center.name) for center in SPORT_CENTRES),
                                 label='Wybierz lokalizację')
    date = forms.DateTimeField(label='Wybierz datę', widget=DateTimePicker())
