from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Post
from book.models import Book


class GetBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
        ]


class GetUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id"
        ]


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "user",
            "book",
            "content"
        ]


class PostListSerializer(ModelSerializer):
    user = GetUserSerializer(read_only=True, many=False)

    class Meta:
        model = Post
        fields = [
            "user",
            "content"
        ]






