from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [

    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/blog/', BlogDetailView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]