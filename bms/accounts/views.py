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