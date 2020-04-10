from django.contrib import admin
from .models import Page

class AdminDefault(admin.ModelAdmin):
    pass

class PageAdmin(admin.ModelAdmin):
	list_display = ['title', 'active', 'pub_date', 'image_img']


admin.site.register(Page, PageAdmin)
