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
        #b = request.data['arg1']+request.data['operator']+request.data['arg2']
        a = eval(request.data["sum"])
        serializer = MathHistorySerializer(data={"sum":request.data["sum"],"result" : a})
        if serializer.is_valid():
            serializer.save()
        return Response({'answer': a})

