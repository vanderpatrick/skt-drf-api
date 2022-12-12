from django.urls import path
from postvideo import views

urlpatterns = [
    path('videos/', views.VideoPostList.as_view()),
]