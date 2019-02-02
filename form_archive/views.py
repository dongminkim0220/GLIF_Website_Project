# basic View
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
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
    template_name = 'form_archive/index.html'
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
class PostDetailView(DetailView):
    model = Post
    template_name = "form_archive/detail.html"
    context_object_name = "post"


@method_decorator([login_required, glifer_required], name='dispatch')
class PostCreateView(UserPassesTestMixin, CreateView):
    model = Post
    template_name = "form_archive/new.html"
    fields = ['title', 'attached_file', 'content']
        
    def get_success_url(self):
        return reverse_lazy('form_archive-index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.writer = Glifer.objects.get(user=self.request.user)
        post.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.glifer.is_authorized

@method_decorator([login_required, glifer_required], name='dispatch')
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "form_archive/update.html"
    fields = ['title', 'attached_file', 'content']

    def test_func(self):
        obj = self.get_object()
        return obj.writer.user == self.request.user

@method_decorator([login_required, glifer_required], name='dispatch')
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "form_archive/delete.html"
    success_url = reverse_lazy('form_archive-index')

    def test_func(self):
        obj = self.get_object()
        return obj.writer.user == self.request.user
    