from rest_framework.serializers import ModelSerializer
from .models import Category, Book


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "category"
        ]


class BookListSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "about",
            "category"
        ]


class BookDetailSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "about",
            "category",
            "file",
            "year",
            "author",
            "page_number",
            "isbn_number",
            "image",
            "free",
            "cost"
        ]







