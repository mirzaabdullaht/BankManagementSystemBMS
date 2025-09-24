from django.urls import path
<<<<<<< HEAD
from .views import BankListAPIView

urlpatterns = [
    path('banks/', BankListAPIView.as_view(), name='banks-list'),
=======
from .views import BankListCreateAPIView, BankDetailAPIView

urlpatterns = [
    path('banks/', BankListCreateAPIView.as_view(), name='bank-list-create'),
    path('banks/<int:pk>/', BankDetailAPIView.as_view(), name='bank-detail'),
>>>>>>> f146474 ( commit — Phase 3 - 6 implementation)
]