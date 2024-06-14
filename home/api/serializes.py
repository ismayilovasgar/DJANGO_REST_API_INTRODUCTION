from rest_framework import serializers
from home.models import *


# class BlogSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=30)
#     content = serializers.CharField(max_length=80)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = "__all__"
        fields = ["id", "title", "content", "created_date", "image", "draft"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = "__all__"
