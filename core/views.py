from django.contrib.auth import login
from django.shortcuts import render,redirect
from base.models import Post
# Create your views here.
from .forms import SignUpForm
def frontpage(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request,'core/frontpage.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})