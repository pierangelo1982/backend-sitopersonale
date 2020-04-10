from django.contrib import admin
from .models import Service

class AdminDefault(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title', 'active', 'pub_date', 'image_img']


admin.site.register(Service, ServiceAdmin)