from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_query, name='search_query'),
]