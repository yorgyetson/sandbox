from django.shortcuts import render, redirect
from django.views import View
from content.models import Post, ContentTag

class ContentDisplay(View):
    """Single post default view"""

    def get(self, request, content_id):
        post = Post.objects.get(pk=content_id)
        latest = Post.objects.all().order_by('updated_at')[:5]
        tags = ContentTag.objects.all()
        return render(request, "pages/content/content_post.html",
                                                            {"title" : title,
                                                            "post" : post,
                                                            "latest" : latest,
                                                            "tags" : tags,})

class ContentDisplayList(View):
    """List recent posts of tag type (default all tags)"""

    def get(self, request, tag=None):
        if tag:
            posts = Post.objects.filter(tags__name=tag).order_by('updated_at')[:5]
            title = tag
        else:
            posts = Post.objects.all().order_by('updated_at')[:5]
            title = "Recent Posts"

        latest = Post.objects.all().order_by('updated_at')[:5]
        tags = ContentTag.objects.all()

        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,
                                                            "latest" : latest,
                                                            "tags" : tags})
