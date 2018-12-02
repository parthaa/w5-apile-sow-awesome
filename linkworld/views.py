from django.shortcuts import render, redirect
from linkworld.models import Post, Comment, Vote
from django.shortcuts import get_object_or_404, resolve_url
from linkworld.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.conf import settings

def index(request):
    posts = list(Post.posts_by_popularity())
    posts_liked_by_user = []
    if request.user.is_authenticated:
        posts_liked_by_user = Post.liked_by_user(request.user)
    page = 1
    if request.GET.get("highlight_id"):
        highlight_post = get_object_or_404(Post, pk=request.GET.get("highlight_id"))
        page = 1 + int(posts.index(highlight_post) / settings.EL_PAGINATION_PER_PAGE)

    return render(request, 'index.html', {'posts': posts,
                        "posts_liked": posts_liked_by_user,
                        "page": page })


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post_detail.html', {
        'post': post,

    })


def new_post(request):

    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            messages.add_message(request, messages.INFO, 'Post Added.')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Post Add Errored.')


    else:
        form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form})


def delete_new_post(request):
    if request.POST.get('pk'):
        post = get_object_or_404(Post, pk=request.POST.get('pk'))
        post.delete()
        messages.add_message(request, messages.INFO, 'Post Deleted.')
        return redirect('home')


def comment_on_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.save()
            messages.add_message(request, messages.INFO, 'Comment Added.')
            return redirect('post_detail', slug=post.slug)

    else:
        form = CommentForm()
    return render(request, 'posts/comment_on_post.html', {'form': form})


def delete_comment(request):
    if request.POST.get('pk'):
        comment = get_object_or_404(Comment, pk=request.POST.get('pk'))
        post = comment.post
        comment.delete()
        messages.add_message(request, messages.INFO, 'Comment Removed.')
        return redirect('post_detail', slug = post.slug )


def upvote(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        if not Vote.objects.filter(post=post, user = request.user).exists():
            Vote.objects.create(post = post, user = request.user)
            messages.add_message(request, messages.INFO, 'You voted.')
        else:
            messages.add_message(request, messages.INFO, 'Already voted.')
        home_url = "{url}?highlight_id={post_id}#{slug}".format(
                        url = resolve_url('home'), slug=post.slug, post_id=post.id)
        return redirect(home_url)
