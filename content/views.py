from django.shortcuts import render, redirect
from django.views import View
from content.models import Post, ContentTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ContentDisplay(View):
    """Single post default view"""

    def get(self, request, content_id):
        post = Post.objects.get(pk=content_id)
        latest = Post.objects.all().order_by('updated_at')[:5]
        tags = ContentTag.objects.all()
        return render(request, "pages/content/content_post.html",
                                                            {"post" : post,
                                                             "latest" : latest,
                                                             "tags" : tags,})

class ContentDisplayList(View):
    """List recent posts of tag type (default all tags)"""

    def get(self, request, tag=None):
        if tag:
            posts = Post.objects.filter(tags__name=tag).order_by('updated_at')
            title = tag
        else:
            posts = Post.objects.all().order_by('updated_at')
            title = "Recent Posts"

        paginator = Paginator(posts, 5) # Show 5 posts per page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)



        latest = Post.objects.all().order_by('updated_at')[:5]
        tags = ContentTag.objects.all()

        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,
                                                            "latest" : latest,
                                                            "tags" : tags})
