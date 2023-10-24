from rest_framework import serializers
from .models import ChatSituation

class ChatSituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSituation
        fields = ['id', 'text', 'created_at']