# Basic View
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy

# Attachment Response
import os
from django.conf import settings
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.utils.http import urlquote

from users.models import Glifer, CustomUser

# Auth
from users.decorator import glifer_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404



@login_required
@glifer_required
def download(request, pk):
    post = Post.objects.get(pk = pk)
    get_file_name = str(post.attached_file).replace("/", "\\")
    filepath = os.path.join(settings.MEDIA_ROOT, get_file_name).replace("\\", "/")    
    attached_file_name = os.path.basename(str(post.attached_file))

    a = attached_file_name
    response = FileResponse(open(filepath, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(urlquote(a))
    print(response['Content-Disposition'])
    return response


@method_decorator([login_required, glifer_required], name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'resume_coaching/index.html'
    context_object_name = "posts"
    paginate_by = 5
    block_size = 5 # 하단의 페이지 목록 수

    
    def get_queryset(self):
        order_by_recent_time = Post.objects.all().order_by("-pk")
        return order_by_recent_time


    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        block_size = 5 # 하단의 페이지 목록 수

        start_index = int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))

        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context

@method_decorator([login_required, glifer_required], name='dispatch')
class PostDetailView(UserPassesTestMixin, DetailView):
    model = Post
    template_name = "resume_coaching/detail.html"
    context_object_name = "post"
    form_class = PostForm

    def test_func(self):
        obj = self.get_object()
        is_writer = obj.writer.user == self.request.user
        is_mentor = self.request.user.glifer.is_mentor
        return (is_writer | is_mentor)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = Glifer.objects.get(user=request.user)
            comment.post = post
            comment.save()
            return redirect('resume_coaching-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'resume_coaching/add_comment_to_post.html', {'form': form})

def edit_comment_to_post(request, pk, pk_comment):
    comment = Comment.objects.get(pk=pk_comment)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance= comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = Glifer.objects.get(user=request.user)
            comment.post = post
            comment.save()
            return redirect('resume_coaching-detail', pk=post.pk)
    else:
        form = CommentForm(instance = comment)
    return render(request, 'resume_coaching/add_comment_to_post.html', {'form': form})

def delete_comment_to_post(request, pk, pk_comment):
    comment = Comment.objects.get(pk=pk_comment)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('resume_coaching-detail', pk=post.pk)
    return render(request, 'resume_coaching/delete_comment_to_post.html')

@method_decorator([login_required, glifer_required], name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = "resume_coaching/new.html"
    fields = ['title', 'attached_file', 'content']

    def get_success_url(self):
        return reverse_lazy('resume_coaching-index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.writer = Glifer.objects.get(user=self.request.user)
        post.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.glifer.is_authorized

@method_decorator([login_required, glifer_required], name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = "resume_coaching/update.html"
    fields = ['title', 'attached_file', 'content']

    def test_func(self):
        obj = self.get_object()
        return obj.writer.user == self.request.user

@method_decorator([login_required, glifer_required], name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = "resume_coaching/delete.html"
    success_url = reverse_lazy('resume_coaching-index')

    def test_func(self):
        obj = self.get_object()
        return obj.writer.user == self.request.user
    