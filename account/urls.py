from django.urls import path
from .views import (
	RegisterUser, 
	UserLogin, 
	ChangePassword,
	login_view,
	)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register user'),
    path('login/', UserLogin.as_view(), name='login user'),
    path('password/change/', ChangePassword.as_view(), name='change password'),
    path('userlogin/', login_view, name='login')


]
