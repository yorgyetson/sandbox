from django.shortcuts import render
from django.views import View
from content.models import Post

class ContentDisplay(View):

    def get(self, request, content_id=None):
        #posts = Posts.objects.all().order_by('start_date')[:5]
        posts = [1]
        title = "Single Content Display"
        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,})

class ContentDisplayList(View):

    def get(self, request, tag=None):
        posts = Post.objects.all().order_by('updated_at')[:5]
        title = "I don't know what to put here"
        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,})
