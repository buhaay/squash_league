from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SportCenter, MyUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'skill')


class CreateReservationForm(forms.Form):
    location = forms.ModelChoiceField(queryset=SportCenter.objects.all(),
                                      empty_label='Wybierz lokalizację')
    date = forms.DateTimeField(label='Wybierz datę')
