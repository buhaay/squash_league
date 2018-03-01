from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

skills = (
    (1, "amator"),
    (2, "okazjonalny grajek"),
    (3, "profesjonalista"),
    (4, "terminator squasha"),
)


class MyUser(AbstractUser):
    skill = models.IntegerField(choices=skills, null=True)


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
    user1 = models.ForeignKey(MyUser, related_name='user1')
    user2 = models.ForeignKey(MyUser, related_name='user2', null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Wybierz dzień')
    time_start = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Początek rezerwacji')
    time_end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Koniec rezerwacji')
    location = models.ForeignKey(SportCenter, verbose_name='Wybierz lokalizację')
    comment = models.CharField(max_length=256, null=True)


def sp_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(sp_pre_save_receiver, sender=SportCenter)