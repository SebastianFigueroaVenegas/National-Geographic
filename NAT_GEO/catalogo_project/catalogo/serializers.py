from rest_framework import serializers
from .models import Movie, ChatMessage

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'sender_username', 'message', 'timestamp', 'is_admin']
