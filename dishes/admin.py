from django.contrib import admin


from dishes.models import Contact, Receipe


@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ('receipe_name','receipe_description')

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','created_at')
    search_fields = ('name', 'email','message')

admin.site.register(Contact, ContactAdmin)

