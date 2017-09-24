from django.contrib import admin
from .models import Post, ContentTag, ContentType

admin.site.register(Post)
admin.site.register(ContentTag)
admin.site.register(ContentType)
