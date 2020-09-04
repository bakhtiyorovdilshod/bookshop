from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book)






