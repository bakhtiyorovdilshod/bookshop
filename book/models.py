from django.db import models


def store_image(instance, filename):
    return './'.join(['images', filename])


def store_file(instance, filename):
    return './'.join(['files', filename])


class Category(models.Model):
    category = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class Book(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=5)
    author = models.CharField(max_length=50)
    about = models.TextField()
    cost = models.PositiveIntegerField()
    page_number = models.PositiveIntegerField()
    isbn_number = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True, upload_to=store_image)
    file = models.FileField(blank=True, null=True, upload_to=store_file)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    free = models.BooleanField(blank=True, null=True, default=False)
    is_new = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


