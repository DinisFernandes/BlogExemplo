from django.shortcuts import render

# Create your views here.

def hello_blog(request):

    lista = [
        'django',
        'Python',
        'Git'
    ]
    data = {'name': 'curso de django', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)
