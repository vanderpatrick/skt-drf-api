from django.urls import path
from videocomments import views

urlpatterns = [
    path('videocomments/', views.VideoCommentList.as_view()),
    path('videocomments/<int:pk>', views.VideoCommentDetail.as_view())
]
