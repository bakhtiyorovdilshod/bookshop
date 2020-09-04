from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Post
from .serializers import PostCreateSerializer, PostListSerializer
from rest_framework.permissions import IsAuthenticated
from book.pagination import BookLimitOffsetPagination


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = BookLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(book__id__icontains=query)


            ).distinct()
        return queryset_list


