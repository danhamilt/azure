from django.db import models
import requests
import json
from langchain.chat_models import ChatOpenAI
from django.conf import settings
from django.utils import timezone

class ChatSituation(models.Model):
    text = models.TextField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    predicted_emotions = models.JSONField(blank=True, null=True)
    last_predicted_update = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.text

    def predict_emotion(self):
        emotions = OpenAI().predict_emotion(self.text)
        self.predicted_emotions = emotions
        self.last_predicted_update = timezone.now()
        self.save()

    @property
    def emotions(self):
        return self.get_emotions()
    
    def get_emotions(self):
        return json.loads(self.predicted_emotions)['emotions']
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.predicted_emotions:
            self.predict_emotion()
class OpenAI:
    def __init__(self) -> None:
        self.api_key = settings.OPENAI_API_KEY
        self.openai = ChatOpenAI(model=settings.DEFAULT_OPENAI_MODEL)
    
    def predict_emotion(self, user_text: str) -> str:
        prompt = f'''You are a psychologist. Our user is in a situation.
                     Situation: {user_text}
                     What emotions do you think this user is feeling?
                     Format your answer in proper json format it should be a json array
                     of emotions. For example: ["sad", "angry", "happy"]
                 '''
        emotions = self.openai.predict(prompt)
        return emotions
