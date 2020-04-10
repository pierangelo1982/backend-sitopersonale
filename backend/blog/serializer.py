from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = (
				'id',
				'title',
				'intro',
				'body',
				'image',
				'tag',
				'active',
				'pub_date'
			)