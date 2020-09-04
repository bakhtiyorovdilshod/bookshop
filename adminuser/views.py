from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny

)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from book.models import Book, Category
from .serializers import (
    UserListSerializer,
    UserDetailListSerializer,
    UserEditListSerializer,
    BookCreateListSerializer,
    CategoryCreateListSerializer
)


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)

            ).distinct()
        return queryset_list


class UserDetailListAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailListSerializer
    permission_classes = [IsAdminUser]


class UserEditListAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserEditListSerializer
    permission_classes = [IsAdminUser]


class UserDeleteListAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailListSerializer
    permission_classes = [IsAdminUser]


class BookCreateListAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateListSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser]
    permission_classes = [IsAdminUser]


class BookListAPIView(ListAPIView):
    serializer_class = BookCreateListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Book.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(category__category__icontains=query) |
                Q(id__icontains=query)

            ).distinct()
        return queryset_list


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateListSerializer
    permission_classes = [IsAdminUser]


class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateListSerializer
    permission_classes = [IsAdminUser]


class BookEditAPIView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateListSerializer
    permission_classes = [IsAdminUser]


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateListSerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateListSerializer
    permission_classes = [IsAdminUser]


class CategoryEditAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateListSerializer
    permission_classes = [IsAdminUser]


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateListSerializer
    permission_classes = [IsAdminUser]


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryCreateListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Category.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(category__icontains=query) |
                Q(id__icontains=query)

            ).distinct()
        return queryset_list






