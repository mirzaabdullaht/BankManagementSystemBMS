from rest_framework import serializers
from .models import BankAccount

class BankAccountSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    class Meta:
        model = BankAccount
        fields = ['id', 'account_number', 'account_type', 'balance', 'is_active', 'user', 'bank_branch']
=======
    bank_name = serializers.CharField(source='bank_branch.bank.name', read_only=True)
    class Meta:
        model = BankAccount
        fields = [
            'id', 'account_number', 'account_type', 'balance', 'is_active', 'bank_name'
        ]
>>>>>>> f146474 ( commit — Phase 3 - 6 implementation)
