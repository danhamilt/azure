from django.urls import path
from .views import chat_situation_list


urlpatterns = [
    path('chat_situation/', chat_situation_list, name='chat_situation_list'),
]