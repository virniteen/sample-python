from django.shortcuts import render
from rest_framework import viewsets
from blogs.models import Category
from blogs.serializers import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
