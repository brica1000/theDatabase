from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import NameForm, PostForm
from .models import Beliefs


def blog_home(request):
    return render(request, 'blog/home.html', {})


def my_beliefs(request):
    posts = Beliefs.objects.all()
    return render(request, 'blog/my_beliefs.html', {'posts': posts})


def edit_beliefs(request):
    post = get_object_or_404(Beliefs)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('my_beliefs'))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_beliefs.html', {'form': form})


def cs_scrape(request):
    return render(request, 'blog/cs_scrape.html', {})
