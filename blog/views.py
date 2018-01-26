from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Post
from .forms import EmailPostForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import redirect


class EmailPostView(View):
    def post(self, request):
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail('Sample Message', 'comment', 'test@test.com', list('mark@rushtonmd.com'))
            return redirect('/admin')

    def get(self, request):
        form = EmailPostForm()
        return render(request, 'blog/post/form1.html', {'form': form})


class PostListView(View):
    def get(self, request):
        # retrieve a list of all published posts
        posts = Post.published.all()

        # the response should render the list.html template,
        # and pass the posts to the template
        return render(request, 'blog/post/list.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, year, month, day, slug):
        # get_object_or_404 retrieves all objects (Posts) from the database
        # that satisfy the QuerySet
        post = get_object_or_404(
            Post,
            slug=slug,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day
        )
        return render(request, 'blog/post/detail.html', {'post': post})
