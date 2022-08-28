from rest_framework import serializers

from .models import *

class StatsSer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"