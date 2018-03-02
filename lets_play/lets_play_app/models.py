from django.contrib.auth.models import AbstractUser
from django.db import models

SKILLS = (
    (1, "Szturmowiec"),
    (2, "Padawan"),
    (3, "Rycerz Jedi"),
    (4, "Mistrz Joda"),
)


class MyUser(AbstractUser):
    skill = models.IntegerField(choices=SKILLS, null=True)


class SportCenter(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    phone_number = models.PositiveIntegerField()
    domain = models.URLField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


class Rooms(models.Model):
    room_number = models.IntegerField()
    sport_center = models.ForeignKey(SportCenter)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.sport_center, self.room_number)


class SquashCourt(models.Model):
    sport_center = models.ForeignKey(SportCenter)
    room_number = models.IntegerField()


class Reservation(models.Model):
    user_main = models.ForeignKey(MyUser, related_name='reservation')
    user_partner = models.ForeignKey(MyUser, related_name='user_partner', null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Wybierz dzień')
    time_start = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Początek rezerwacji')
    time_end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Koniec rezerwacji')
    location = models.ForeignKey(SportCenter, verbose_name='Wybierz lokalizację')
    comment = models.CharField(max_length=256, null=True)


