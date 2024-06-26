from django.urls import path
from .views import *

app_name = "blog"
urlpatterns = [
    # Blog
    path("list/", BlogListAPIView.as_view(), name="api-list"),
    path("create/", BlogCreateAPIView.as_view(), name="api-create"),
    path("detail/<pk>", BlogDetailAPIView.as_view(), name="api-detail"),
    path("delete/<pk>", BlogDeleteAPIView.as_view(), name="api-delete"),
    path("update/<pk>", BlogUpdateAPIView.as_view(), name="api-update"),
]
