from django.urls import path
from videodislike import views

urlpatterns = [
    path('videodislikes/', views.VideoDislikeList.as_view()),
    path('videodislikes/<int:pk>', views.VideoDislikeDetail.as_view()),
]
