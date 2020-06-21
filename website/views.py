from django.shortcuts import render, get_object_or_404
from .models import Post, Contact
from urllib.parse import quote_plus

# Create your views here.

def hello_blog(request):

    lista = [
        'django',
        'Python',
        'Git'
    ]
    list_posts = Post.objects.all()
    data = {'name': 'curso de django',
            'lista_tecnologias': lista,
            'posts': list_posts
            }

    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post_detail.html', context)


def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name=name,
        email=request.POST['email'],
        message=request.POST['message']
    )

    return render(request, 'contact_success.html',{'name_contact': name})

def post_share_fb(request, id):
    post = Post.objects.get(id=id)
    share_string = quote_plus(post.imagem.url)
    context = {'post':post,
        'share_string': share_string
    }

    return render(request, 'post_share_fb.html', context)