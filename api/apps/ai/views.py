from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ChatSituation
from .serializers import ChatSituationSerializer

@api_view(['GET', 'POST'])
def chat_situation_list(request):
    if request.method == 'GET':
        chat_situations = ChatSituation.objects.all()
        serializer = ChatSituationSerializer(chat_situations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChatSituationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)