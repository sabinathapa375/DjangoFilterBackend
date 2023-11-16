from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

#Locally using the DjangoFilterBackend
# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    #showing the data of the user that logs in. 
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby = user)
    
    #Locallly using djangofilterbackend
    # filter_backends = [DjangoFilterBackend] 
    
    filterset_fields = ['address']
    
    
