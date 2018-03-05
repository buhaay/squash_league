from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MyUser)
admin.site.register(SportCenter)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(UserStats)

