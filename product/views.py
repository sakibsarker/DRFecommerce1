from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from .serializers import CategorySerilizer,Product,BrandSerilizer
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category,Product,Brand


class CategoryView(viewsets.ViewSet):
    "A simple view for viewing categories"

    queryset=Category.objects.all()

    @extend_schema(responses=CategorySerilizer)
    def list(self,request):
        serializer=CategorySerilizer(self.queryset,many=True)
        return Response(serializer.data)