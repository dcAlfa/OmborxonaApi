from rest_framework import serializers

from .models import *

class OmborSer(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = "__all__"