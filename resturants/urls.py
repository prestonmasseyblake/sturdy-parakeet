from django.urls import path 
from .views import ResturantView
from resturants import views

urlpatterns = [
    path('',ResturantView.as_view({'get':'list'}))
]