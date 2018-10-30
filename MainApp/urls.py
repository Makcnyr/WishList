from django.views.generic import ListView, DetailView
from MainApp.models import WishList
from django.urls import path

urlpatterns = [
    path('', ListView.as_view(queryset=WishList.objects.all(),
                             template_name="MainApp/HomePage.html")),
]