from django.urls import path
from .views import (
	CategoryList, 
	FreeBookList, 
	BookList, 
	BookDetailList, 
	HomePage, 
	BookDetailView,
	BookListView,
	BookFilter,
	ContactForm
)


urlpatterns = [
    path('category/', CategoryList.as_view(), name='category list'),
    path('free/', FreeBookList.as_view(), name='free book list'),
    path('', BookList.as_view(), name='category book'),
    path("<int:pk>/", BookDetailList.as_view(), name='detail of book'),
    path("home", HomePage.as_view(), name='home'),
    path('home/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('free/book/',BookListView.as_view(), name='free' ),
    path('book/filter/', BookFilter, name='filter' ),
    path('contact/', ContactForm, name='contact')


]
