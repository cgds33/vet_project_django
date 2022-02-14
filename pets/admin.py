from django.contrib import admin
from .models import Pet
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    
    # Pet model for admin panel
    list_display = ["petType","petName","author"]
    list_display_links = ["petType","petName"]
    search_fields = ["petName","author"]
    list_filter = ["createdDate"]

    # Built based on django recommendations 
    class Meta:
        model = Pet

