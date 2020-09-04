from django.urls import path
from .views import PostCreateAPIView, PostListAPIView

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='post create'),
    path('list/', PostListAPIView.as_view(), name='post list'),

]