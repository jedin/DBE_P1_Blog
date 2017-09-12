from django.shortcuts import render, get_object_or_404
from .models import Post


# Display lists of posts
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',  # template path
                  {'posts': posts})  # variables to render template


# Display a single post
# Retrieve a post with given slug and date
def post_detail(request, year, month, day, post):
    # Get object matching parameters or return HTTP 404 exception
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
