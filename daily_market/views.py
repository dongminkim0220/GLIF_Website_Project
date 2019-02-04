# basic view
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# pdf
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin

# id
from users.models import Glifer, CustomUser
from django.http import HttpResponseRedirect

# Permissions
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import PostForm

class CreateReport(PDFTemplateResponseMixin, DetailView):
    template_name = 'daily_market/pdf_template.html'
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        return super(CreateReport, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            encoding = u"utf-8",
            **kwargs
        )

    def get_pdf_response(self, context, **kwargs):
        return super(CreateReport, self).get_pdf_response(
            context,
            **kwargs,
            charset = "utf-8",
        )

class PostListView(ListView):
    model = Post
    template_name = 'daily_market/index.html'
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
    template_name = "daily_market/detail.html"
    context_object_name = "post"

class PostCreateView(UserPassesTestMixin, CreateView):
    model = Post
    template_name = "daily_market/new.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('daily_market-index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.writer = Glifer.objects.get(user=self.request.user.glifer)
        post.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def test_func(self):
        return self.request.user.glifer.is_authorized
        
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "daily_market/update.html"
    form_class = PostForm
    success_url = reverse_lazy('daily_market-index')

    def test_func(self):
        obj = self.get_object()
        return obj.writer.user == self.request.user

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "daily_market/delete.html"
    success_url = reverse_lazy('daily_market-index')

    def test_func(self):
        obj = self.get_object()
        return obj.writer.user == self.request.user
    