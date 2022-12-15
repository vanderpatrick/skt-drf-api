
from django.urls import path
from videofavorites import views

urlpatterns = [
    path('videofavorites/', views.VideofavoritesList.as_view()),
    path('videofavorites/<int:pk>/', views.VideofavoritesDetail.as_view()),
]
