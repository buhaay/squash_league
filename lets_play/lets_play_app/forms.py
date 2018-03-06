from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions

from .models import SportCenter, MyUser, Reservation, Score

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
    time_end = forms.ChoiceField((x, str(x) + ':00') for x in range(11, 24))
    class Meta:
        model = Reservation
        fields = ['date', 'location']
        widgets = {'date': DateInput()}


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['user_main_score', 'user_partner_score']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'skill', 'avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 200
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar
