from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    """
    List of fields shown on the admin dashboard
    """ 
    list_display = (
        'title',
        'slug',
        'date_added',
    )

    search_fields = (
        'title',
    )

    list_per_page = 20
    
    # orders messages by most recent
    ordering = ('-date_added',)


admin.site.register(Post, BlogAdmin)
