from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # post details
    path('post/<slug>', views.post_detail, name="blog-post-detail"),
]