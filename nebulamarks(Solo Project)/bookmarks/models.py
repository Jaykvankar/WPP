from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    DEFAULT_NAME = "General"

    def __str__(self):
        return self.name

    @staticmethod
    def get_default():
        category, created = Category.objects.get_or_create(name=Category.DEFAULT_NAME)
        return category

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=Category.get_default)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
