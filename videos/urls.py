from django.urls import path
from videos import views

urlpatterns = [
    path('videos/', views.VideoList.as_view()),
]
