from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from book.models import Book, Category


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email"
        ]


class UserDetailListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserEditListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "is_superuser",
            "email",
            "is_staff",
            "is_active"

        ]


class BookCreateListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CategoryCreateListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



