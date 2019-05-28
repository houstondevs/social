from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import AddPost
from django.http import JsonResponse

def post_list(request):
    if request.is_ajax():
        post_form = AddPost(request.POST)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {
                'message': 'form is saved'
            }
            return JsonResponse(data)
    else:
        post_form = AddPost()

    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'app_blog/posts_list.html', {'posts':posts, 'post_form':post_form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app_blog/post_detail.html', {'post':post})


