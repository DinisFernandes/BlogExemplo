from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'categories', 'actived']
    search_fields = ['title', 'subtitle']
    #fields = ['title', 'subtitle']

    def get_queryset(self, request):
        return Post.objects.all()

admin.site.register(Post, PostAdmin)


