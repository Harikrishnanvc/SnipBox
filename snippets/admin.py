from django.contrib import admin
from snippets.models import Snippets, Tag
# Register your models here.

admin.site.register(Snippets)
admin.site.register(Tag)