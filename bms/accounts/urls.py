<<<<<<< HEAD
from django.urls import path
from .views import UserAccountsAPIView

urlpatterns = [
    path('accounts/', UserAccountsAPIView.as_view(), name='user-accounts'),
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('banks.urls')),
    path('api/', include('accounts.urls')),
>>>>>>> f146474 ( commit — Phase 3 - 6 implementation)
]