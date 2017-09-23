from django.shortcuts import render
from django.views import View

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
        #posts = Posts.objects.all().order_by('start_date')[:5]
        posts = [1,2,3]
        title = "Display Content List"
        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,})
