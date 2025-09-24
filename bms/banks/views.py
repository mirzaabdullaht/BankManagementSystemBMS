<<<<<<< HEAD
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank
from .serializers import BankSerializer

class BankListAPIView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)
=======
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Bank
from .serializers import BankSerializer

class BankListCreateAPIView(ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
>>>>>>> f146474 ( commit — Phase 3 - 6 implementation)
