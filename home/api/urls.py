from django.urls import path
from .views import ItemDetail, ItemList
from .views import *


urlpatterns = [
    # Blog
    # path("list/", BlogListAPIView.as_view(), name="api-list"),
    # path("detail/<pk>", BlogDetailAPIView.as_view(), name="api-detail"),
    # path("delete/<pk>", BlogDeleteAPIView.as_view(), name="api-delete"),
    # path("update/<pk>", BlogUpdateAPIView.as_view(), name="api-update"),
    # Employee
    # path("insertempapi/", saveemp, name="saveemp"),
    # path("insertemp/", insertemp, name="insertemp"),
    # path("insertemp-list/", listinsertemp, name="listinsertemp"),
    # path("listemp/", listemp.as_view(), name="listemp"),
    #
    path("list/", ItemList.as_view()),
    path("detail/<int:pk>", ItemDetail.as_view()),
    path("add-movie", add_movie, name="add-movie"),
]
