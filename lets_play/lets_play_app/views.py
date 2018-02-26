from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.
from django.views import View

from lets_play_app.forms import SignUpForm


class HomeView(View):
    def get(self, request):
        return render(request, 'base.html', {})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')


class ShowProfileView(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        return render(request, 'show_profile.html', {"user": user})


