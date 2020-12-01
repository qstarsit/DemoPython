from .models import MathHistory
from .serializers import MathHistorySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class MathAPIViewSet(viewsets.ModelViewSet):
    queryset = MathHistory.objects.all()
    serializer_class = MathHistorySerializer

    def perform_create(self, serializer):
            serializer.save()

    @action(detail=False, methods=['post'])
    def do_sum(self, request, pk=None):
        #Hier mist het verwerken van de data!
        #
        #
        #
        #
        #
        #
        serializer = MathHistorySerializer(data={"sum": # Hier mist de som voor de DB ,"result" : # Hier mist het resultaat})
        #Dit slaat je data op in de DB 
        if serializer.is_valid():
            serializer.save()
        return Response({'answer': # Hier mist het resultaat })

