from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class StatsApiView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        s = Stats.objects.filter(ombor=ombor)
        ser = StatsSer(s, many=True)
        return Response(ser.data)

    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = StatsSer(data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
        return Response(ser.data)
class StatsRUD(APIView):
    def delete(self,request, pk):
        o = Ombor.objects.get(user=request.user)
        s = Stats.objects.get(id=pk)
        if s.ombor==o:
            s.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        s = Stats.objects.get(id=pk)
        serializer = StatsSer(s,data=request.data)
        if serializer.is_valid():
            serializer.save(ombor=o)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)