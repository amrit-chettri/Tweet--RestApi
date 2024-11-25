from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id','text', 'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        tweet = Tweet.objects.create(user=user, **validated_data)
        return tweet