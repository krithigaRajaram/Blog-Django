
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
from .models import Post
def detail(request,  slug):
    post = get_object_or_404(Post, slug=slug)

  
    return render(request, 'base/detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', slug=post.slug)  # Redirect to the newly created post detail page
    else:
        form = PostForm()
    return render(request, 'base/create.html', {'form': form})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query))

    return render(request, 'base/search.html', {'posts': posts, 'query': query})