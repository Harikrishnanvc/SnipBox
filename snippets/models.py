from django.contrib.auth.models import User
from django.db import models


class MasterModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class Tag(MasterModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Snippets(MasterModel):
    title = models.CharField(max_length=255)
    note = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
