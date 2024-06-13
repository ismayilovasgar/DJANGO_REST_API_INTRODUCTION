from ..forms import *

from ..models import Blog
from .serializes import *
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render

from rest_framework import generics
from .serializes import *


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


# def add_movie(request):
#     context = dict()
#     url = request.META.get("HTTP_REFERER")
#     if request.method == "POST":
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(url)

#     else:
#         context["form"] = MovieForm()

#     return render(request, "add_movie.html", context)
