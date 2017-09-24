from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from tinymce.models import HTMLField
from geek_beacon.users.models import User


class Post(models.Model):
    """Table to hold posts"""

    title = models.CharField(max_length=1000)
    body = HTMLField()
    description = HTMLField()
    author = models.ForeignKey(User)
    thumbnail_image = models.ImageField(upload_to='content/thumbs/', blank = True)
    header_image = models.ImageField(upload_to='content/headers/', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    tags = models.ManyToManyField('ContentTag')
    content_type = models.ManyToManyField('ContentType')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'content'
        db_table = 'content_post'


class ContentTag(models.Model):
    """Table to hold the content tags"""

    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'content'
        db_table = 'content_tag'


class ContentType(models.Model):
    """Table to hold the content types"""

    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'content'
        db_table = 'content_type'
