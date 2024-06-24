from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apiapp.models import User
from apiapp.serializers import *

# Create your views here.


class Userview(APIView):

    serializer_class = Userserializer

    def get(self, request):
        users= User.objects.all().values()
        return Response({  "all users":users}  )

    def post (self, request):

        serializer_obj = Userserializer(data= request.data)

        if(serializer_obj.is_valid()):

            User.objects.create(name=request.data["name"],
                                age = request.data["age"],
                                salary = request.data["salary"],)

        users = User.objects.all().filter(name=request.data["name"].values())
        return Response({"Message":"New user added", "User": users})