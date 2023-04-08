from django.contrib import admin
from .models import Post

# Register class in admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'order',]
