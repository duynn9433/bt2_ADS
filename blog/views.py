from django.shortcuts import render

# Create your views here.
from blog.models import Post


def list(request):
    data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', data)


def post(request, id=None):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})