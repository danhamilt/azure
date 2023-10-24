from django.urls import path
from .views import ChatSituationListCreateAPIView

urlpatterns = [
    path('chat_situation/', ChatSituationListCreateAPIView.as_view(), name='chat_situation_list_create'),
]