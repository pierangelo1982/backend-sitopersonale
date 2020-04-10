from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'active', 'pub_date', 'image_img']


admin.site.register(Post, PostAdmin)
