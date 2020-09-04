from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 4
