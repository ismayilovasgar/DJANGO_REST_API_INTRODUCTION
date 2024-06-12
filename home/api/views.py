from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from ..forms import *

# from ..models import Blog
# from .serializes import *
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     DestroyAPIView,
#     UpdateAPIView,
# )
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.response import Response
# import requests
from django.shortcuts import render

from rest_framework import generics
from .serializes import *

# class BlogListAPIView(ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogDetailAPIView(RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = "pk"


# class BlogDeleteAPIView(DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = "pk"


# class BlogUpdateAPIView(UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = "pk"


# @api_view(["POST"])
# def saveemp(request):
#     if request.method == "POST":
#         saveserializer = EmployeeSerializer(data=request.data)
#         if saveserializer.is_valid():
#             saveserializer.save()
#             return Response(saveserializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(saveserializer.data, status=status.HTTP_400_BAD_REQUEST)


# def insertemp(request):
#     context = dict()
#     url = request.META.get("HTTP_REFERER")
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(url)
#     else:
#         context["form"] = EmployeeForm()
#         return render(request, "insertdata.html", context)


# def listinsertemp(request):
#     data = EmployeeSerializer(Employeemodel.objects.all(), many=True).data
#     return JsonResponse(data, safe=False)


# class listemp(ListAPIView):
#     queryset = Employeemodel.objects.all()
#     serializer_class = EmployeeSerializer


# * Movie API
class ItemList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = MovieModel.objects.all()
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()


def add_movie(request):
    context = dict()
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(url)

    else:
        context["form"] = MovieForm()

    return render(request, "add_movie.html", context)
