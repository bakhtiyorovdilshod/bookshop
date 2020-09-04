from django.urls import path
from .views import (
    UserListAPIView,
    UserDetailListAPIView,
    UserEditListAPIView,
    UserDeleteListAPIView,
    BookCreateListAPIView,
    BookListAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    BookDeleteAPIView,
    BookEditAPIView,
    BookDetailAPIView,
    CategoryDetailAPIView,
    CategoryDeleteAPIView,
    CategoryEditAPIView,
)

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='all users'),
    path('users/<int:pk>/', UserDetailListAPIView.as_view(), name='user detail'),
    path('users/<int:pk>/edit/', UserEditListAPIView.as_view(), name='user edit'),
    path('users/<int:pk>/delete/', UserDeleteListAPIView.as_view(), name='delete user'),
    path('book/create/', BookCreateListAPIView.as_view(), name='book create'),
    path('books/', BookListAPIView.as_view(), name='all books'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='create category'),
    path('categories/', CategoryListAPIView.as_view(), name='all categories'),
    path('category<int:pk>/edit/', CategoryEditAPIView.as_view(), name='edit category'),
    path('category<int:pk>/', CategoryDetailAPIView.as_view(), name='detail of category'),
    path('category<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name='delete category'),
    path('book/<int:pk>/edit', BookEditAPIView.as_view(), name='edit book'),
    path('book/<int:pk>/detail/', BookDetailAPIView.as_view(), name='detail book'),
    path('book/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='delete book'),


]

