from .views import hello_blog
from django.urls import path


urlpatterns = [
    path('', hello_blog),
]