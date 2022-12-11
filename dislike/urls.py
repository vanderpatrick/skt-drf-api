from django.urls import path
from dislike import views

urlpatterns = [
    path('dislikes/', views.DislikeList.as_view()),
    path('dislikes/<int:pk>', views.DislikeDetail.as_view()),
]
