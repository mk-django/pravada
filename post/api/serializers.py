from rest_framework import serializers
from post.models import Post

# JSON Conversion and Validation
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['__all__']
