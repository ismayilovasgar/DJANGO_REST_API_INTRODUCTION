from rest_framework import serializers
from home.models import *


# class BlogSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=30)
#     content = serializers.CharField(max_length=80)


class BlogSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="blog:api-detail",
        lookup_field="pk",
    )

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return f"{obj.user.username}"

    class Meta:
        model = Blog
        # fields = "__all__"
        fields = [
            "url",
            "username",
            "title",
            "content",
            "created_date",
            "image",
            "draft",
        ]
        # fields = ["id","username" ,"title", "content", "created_date", "image", "draft"]


class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        # fields = "__all__"
        # fields = ["url", "title", "content", "created_date", "image", "draft"]
        fields = ["id", "title", "content", "created_date", "image", "draft"]


class MovieSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return f"{obj.user.username}"

    class Meta:
        model = MovieModel
        fields = [
            "id",
            "username",
            "movie_name",
            "image_url",
            "director",
            "content",
            "release_year",
        ]
