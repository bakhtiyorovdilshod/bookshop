from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login, logout
import json
from .forms import UserLoginForm
from django.shortcuts import render


@permission_classes((AllowAny,))
class RegisterUser(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        mail = data['email']
        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username, mail, password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return Response("User is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = json.loads(request.body.decode("UTF-8"))
        username = data['username']
        password = data['password']
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'status': user.is_superuser})


@permission_classes((IsAuthenticated,))
class ChangePassword(APIView):
    def post(self, request):
        data = json.loads(request.body)
        new_password = data['new_password']
        old_password = data['old_password']
        auth = str(request.META['HTTP_AUTHORIZATION'])
        token_filter = Token.objects.get(key=auth)
        user_id = token_filter.user_id
        user = authenticate(username=token_filter.user, password=old_password)
        if user:
            user_change_password = User.objects.get(pk=int(user_id))
            user_change_password.set_password(new_password)
            user_change_password.save()
            return Response("Password is created successfully")
        else:
            return Response("Old password is not correct")


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
    
        password = form.cleaned_data.get("password")
	
        
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, "account/login.html", {"form":form})






