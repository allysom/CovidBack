from django.contrib import admin
    
from .models import Exame

class ExameAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Exame._meta.fields ]

admin.site.register(Exame, ExameAdmin)
