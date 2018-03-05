"""lets_play URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lets_play_app.views import SignUpView, HomeView, ShowProfileView, CreateReservationView,\
    SportCenterDetailView, SportCenterListView, JoinRoomView, ReservationDetailView, DeleteRoom, UserRoomsView, UserHistoryView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^profile/(?P<user_id>[0-9]+)$', ShowProfileView.as_view(), name='profile'),
    url(r'^create_reservation/$', CreateReservationView.as_view(), name='create_reservation'),
    url(r'^sport_center/(?P<slug>[\w-]+)$', SportCenterDetailView.as_view(), name='sp_detail'),
    url(r'^sport_centres/$', SportCenterListView.as_view(), name='create_room'),
    url(r'^rooms/$', JoinRoomView.as_view(), name='rooms'),
    url(r'^rooms/(?P<room_id>[\d]+)$', ReservationDetailView.as_view(), name='room'),
    url(r'^delete_room/(?P<room_id>[\d]+)$', DeleteRoom.as_view(), name='delete_room'),
    url(r'^user_reservations/$', UserRoomsView.as_view(), name='user_rooms'),
    url(r'^user_history/$', UserHistoryView.as_view(), name='user_history'),

    #reset password
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


]
