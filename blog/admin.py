from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'published', 'text', 'image', 'link']
    search_fields = ['title']
    list_filter = ['published']
    list_display = ['title', 'published', 'image', 'link']
    list_editable = ['published']
admin.site.register(Post, PostAdmin)
