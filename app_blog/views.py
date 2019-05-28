from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app_blog/posts_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app_blog/post_detail.html', {'post':post})