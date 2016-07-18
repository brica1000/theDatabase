from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm, PostForm
from .models import Beliefs


def my_beliefs(request):
    posts = Beliefs.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('blog/my_beliefs.html')
        else:
            form = PostForm()
    return render(request, 'blog/my_beliefs.html', {'posts': posts, 'form': form})

def blog_home(request):
    return render(request, 'blog/home.html', {})
