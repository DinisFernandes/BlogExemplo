from .views import hello_blog, post_detail
from django.urls import path


urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>', post_detail, name='post_detail'),
]