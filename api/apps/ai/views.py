from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatSituation
from .serializers import ChatSituationSerializer

class ChatSituationListCreateAPIView(APIView):
    def get(self, request):
        chat_situations = ChatSituation.objects.all()
        serializer = ChatSituationSerializer(chat_situations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatSituationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)