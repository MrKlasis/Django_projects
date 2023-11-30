from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'text', 'img', 'activate')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'text', 'img', 'activate')
    # success_url = reverse_lazy('catalog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    extra_context = {
        'title': 'Блог',
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(activate=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        blog_item = Blog.objects.get(pk=self.kwargs.get('pk'))
        context_data['blog_pk'] = blog_item.pk,
        context_data['title'] = f'{blog_item.title}(slug = {blog_item.slug})'

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object
