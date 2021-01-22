from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    List of fields shown on the admin dashboard
    """ 
    list_display = (
        'user_id',
        'full_name',
        'email',
        'contact_date',
    )

    search_fields = (
        'full_name',
        'email',
    )

    list_per_page = 20
    
    # orders messages by most recent
    ordering = ('-contact_date',)


admin.site.register(Contact, ContactAdmin)
