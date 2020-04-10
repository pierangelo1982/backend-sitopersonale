from django.contrib import admin
from .models import Slider



class SliderAdmin(admin.ModelAdmin):
	list_display = ['title', 'active', 'pub_date', 'image_img']


admin.site.register(Slider, SliderAdmin)