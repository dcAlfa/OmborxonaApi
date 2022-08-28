from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import *
from .models import *
from .serializers import *



class ClienApiView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        clientlar = Client.objects.filter(ombor=ombor)
        ser = ClientSer(clientlar, many=True)
        return Response(ser.data)
    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = ClientSer(data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
        return Response(ser.data)

class ClientRUD(APIView):
    def delete(self,request, pk):
        o = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        if client.ombor==o:
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        serializer = ClientSer(client,data=request.data)
        if serializer.is_valid():
            serializer.save(ombor=o)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MahsulotApiView(APIView):
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        m = Maxsulot.objects.filter(ombor=ombor)
        ser = MahsulotSer(m, many=True)
        return Response(ser.data)

    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        malumot = request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            ser.save(ombor=o)
        return Response(ser.data)


class MahsulotRUD(APIView):
    def delete(self,request, pk):
        o = Ombor.objects.get(user=request.user)
        mahsulot = Maxsulot.objects.get(id=pk)
        if mahsulot.ombor==o:
            mahsulot.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        m = Maxsulot.objects.get(id=pk)
        serializer = MahsulotSer(m,data=request.data)
        if serializer.is_valid():
            serializer.save(ombor=o)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

