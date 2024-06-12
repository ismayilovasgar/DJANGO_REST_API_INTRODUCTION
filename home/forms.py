from django.forms import ModelForm, TextInput, EmailInput
from .models import *


class MovieForm(ModelForm):

    class Meta:
        model = MovieModel
        fields = "__all__"
