<<<<<<< HEAD
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BankAccount
from .serializers import BankAccountSerializer

class UserAccountsAPIView(APIView):
    def get(self, request):
        # For demo, show all accounts (should filter by user)
        accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(accounts, many=True)
        return Response(serializer.data)
=======
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BankAccount
from .serializers import BankAccountSerializer
from rest_framework.permissions import IsAuthenticated

class AccountListCreateAPIView(ListCreateAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Show only current user's accounts
        return BankAccount.objects.filter(user=self.request.user)

class AccountDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Show only current user's accounts
        return BankAccount.objects.filter(user=self.request.user)
>>>>>>> f146474 ( commit — Phase 3 - 6 implementation)
