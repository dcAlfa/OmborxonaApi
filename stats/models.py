from django.db import models

from asosiy.models import *

from user.models import Ombor


class Stats(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    umumiy = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    miqdor = models.PositiveSmallIntegerField()
    nasiya = models.PositiveSmallIntegerField()
    sana = models.DateField(auto_now_add=True)
    foyda = models.PositiveSmallIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.ism