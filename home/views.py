from django.shortcuts import render
from .forms import *
from .models import *
from .api.serializes import *
from rest_framework import generics


# Create your views here.
# * Movie API
class ItemList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = MovieModel.objects.all()
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()


def show__movies(request):
    return render(request, "view.html")
