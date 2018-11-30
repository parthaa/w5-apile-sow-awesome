from django.shortcuts import render, redirect
from linkworld.models import Post, Comment
from django.shortcuts import get_object_or_404
from linkworld.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, UserSerializer


def index(request):
    posts = Post.objects.all().order_by("-date")
    comments = Comment.objects.all().order_by("-date")
    return render(request, 'index.html', {'posts': posts, 'comments': comments, })


def post_detail(request, slug):

    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post_detail.html', {
        'post': post,

    })


def new_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form})


def comment_on_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'posts/comment_on_post.html', {'form': form})



class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer