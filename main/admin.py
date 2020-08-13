from django.contrib import admin
from .models import SaiArts

# Register your models here.
@admin.register(SaiArts)
class SAIARTAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'artist', 'publish_date', 'timestamp', 'body')
    list_filter = ('artist', 'name')
    prepopulated_fields={'slug':('name',)} 
    ordering = ('timestamp',)
