from django.db import models

from user.models import Ombor


class Client(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    dokon = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    qarz = models.PositiveSmallIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
         return self.ism

class Maxsulot(models.Model):
    nom = models.CharField(max_length=100)
    miqdor = models.PositiveSmallIntegerField()
    brend = models.CharField(max_length=100)
    kelgan_narx = models.PositiveSmallIntegerField()
    sotuvdagi_narx = models.PositiveSmallIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

