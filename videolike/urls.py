from django.urls import path
from videolike import views

urlpatterns = [
    path('videolikes/', views.VideoLikeList.as_view()),
    path('videolikes/<int:pk>', views.VideoLikeDetail.as_view()),
]
