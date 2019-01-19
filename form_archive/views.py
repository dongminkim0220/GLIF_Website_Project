from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
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

class PostDetailView(DetailView):
    model = Post
    template_name = "form_archive/detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    template_name = "form_archive/new.html"
    fields = "__all__"
    success_url = reverse_lazy('form_archive-index')

class PostUpdateView(UpdateView):
    model = Post
    template_name = "form_archive/update.html"
    fields = ['title', 'attached_file', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "form_archive/delete.html"
    success_url = reverse_lazy('form_archive-index')
    