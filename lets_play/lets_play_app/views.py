import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import SportCenter, Reservation, MyUser
from .forms import CreateReservationForm, SignUpForm


# Create your views here.
from django.views import View
from django.views.generic import FormView, DetailView


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})


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
        else:
            return HttpResponse(str(form.errors))


class ShowProfileView(View):
    def get(self, request, user_id):
        user = MyUser.objects.get(pk=user_id)
        return render(request, 'show_profile.html', {"user": user})


class CreateReservationView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateReservationForm()
        return render(request, 'create_reservation.html', {'form': form})

    def post(self, request):
        form = CreateReservationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            date = form.cleaned_data['date']
            time_start = form.cleaned_data['time_start']
            time_end = form.cleaned_data['time_end']
            date_to_check = datetime.datetime.combine(date=date, time=time_start).timestamp()
            now = datetime.datetime.now().timestamp()
            if date_to_check < now:
                message = 'Wybierz datę z przyszłości'
                return render(request, 'create_reservation.html', {'message': message,
                                                                   'form': form})
            Reservation.objects.create(user1=request.user, location=location, date=date,
                                       time_start=time_start, time_end=time_end)
            return redirect(reverse('home'))


class SportCenterListView(View):
    def get(self, request):
        sport_centres = SportCenter.objects.all()
        return render(request, 'sport_centres_list.html', {'sport_centres': sport_centres})


class SportCenterDetailView(DetailView):
    queryset = SportCenter.objects.all()
    def get_context_data(self, **kwargs):
        print(self.kwargs)
        context = super(SportCenterDetailView, self).get_context_data(**kwargs)
        print(context)
        return context


class JoinRoomView(LoginRequiredMixin, View):
    def get(self, request):
        rooms = Reservation.objects.filter(user2__isnull=True).exclude(user1=request.user)
        return render(request, 'room_list.html', {'rooms': rooms})


class ReservationDetailView(View):
    def get(self, request, room_id):
        room = Reservation.objects.get(pk=room_id)
        return render(request, 'room_detail.html', {'room': room})

    def post(self, request, room_id):
        room = Reservation.objects.get(pk=room_id)
        if room.user2_id is None:
            room.user2_id = request.user.id
            room.save()
            return redirect('rooms')
        else:
            message = "Pokój gry jest pełny, wybierz inny termin"
            ctx = {'message': message}
            return render(request, 'full_room.html', ctx)














