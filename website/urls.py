from .views import hello_blog, post_detail, save_form, post_share_fb
from django.urls import path


urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('save-form/', save_form, name='save_form'),
    path('post/<int:id>/facebookshare/', post_share_fb, name='post_share_fb'),
]