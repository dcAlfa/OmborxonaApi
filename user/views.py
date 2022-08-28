from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class OmborApiView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        ser = OmborSer(ombor)
        return Response(ser.data)
    def post(self,request):
        ombor = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = OmborSer(data=malumot)
        if ser.is_valid():
            if ombor.user == request.user:
                ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class OmborRUD(APIView):
    def delete(self,request, pk):
        om = Ombor.objects.get(user=request.user)
        o = Ombor.objects.get(id=pk)
        if o==om:
            o.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        om = Ombor.objects.get(user=request.user)
        o = Ombor.objects.get(id=pk)
        serializer = OmborSer(o,data=request.data)
        if serializer.is_valid():
            if o==om:
                serializer.save(user=request.user)
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

