from django.urls import path
from . import views

# mapping the root url to the index function by passing a ref to that func
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
