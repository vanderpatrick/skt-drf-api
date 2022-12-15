
from django.urls import path
from favorites import views

urlpatterns = [
    path('favorites/', views.PostFavoritesList.as_view()),
    path('favorites/<int:pk>/', views.PostFavoritesDetail.as_view()),
]
