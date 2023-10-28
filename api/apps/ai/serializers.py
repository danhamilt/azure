from rest_framework import serializers
from .models import ChatSituation

class ChatSituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSituation
        fields = ['id', 'text', 'created_at', 'emotions', 'last_predicted_update']

    def get_emotions(self, obj):
        return obj.get_emotions