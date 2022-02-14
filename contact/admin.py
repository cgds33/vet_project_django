from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    # Contact model for admin panel
    list_display = ["author","email","phone"]
    list_display_links = ["author"]
    search_fields = ["author","email","phone"]

    # Built based on django recommendations 
    class Meta:
        model = Contact
