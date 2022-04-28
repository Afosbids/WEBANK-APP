
from django.shortcuts import render,HttpResponse
from rest_framework import generics
# from rest_framework.permissions import isAunthenticated, AllowAny
from weBankAPI.serializers import UserSerializer
from .models import User


def home(request):
    return HttpResponse('<h1>weBank Project Setup, Docker works fine :-)  </h1>')



# Create your views here.
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = isAunthenticated
    

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.get()
    serializer_class = UserSerializer
    