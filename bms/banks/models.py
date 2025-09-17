# Create your models here.
from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=20)
    is_islamic = models.BooleanField(default=False)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class BankBranch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.bank.name})"