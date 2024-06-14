from ..forms import *

from ..models import Blog
from .serializes import *
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
)
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render

from rest_framework import generics
from .serializes import *

# DRF 2
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import *


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["id"]

    # pagination_class = BlogPagination

    # def get_queryset(self):
    #     return Blog.objects.filter(draft=True)


class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = "pk"


class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# * DRF Part 2
# class BlogListAPIView(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
