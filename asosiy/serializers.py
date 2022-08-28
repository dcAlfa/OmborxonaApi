from rest_framework import serializers

from .models import *

class ClientSer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MahsulotSer(serializers.ModelSerializer):
    class Meta:
        model = Maxsulot
        fields = "__all__"