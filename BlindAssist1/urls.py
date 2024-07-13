from django.urls import path
from . views import LoginView, CustomRegisterAPIView, ProvidingDescription

urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('register/', CustomRegisterAPIView.as_view(), name='custom_register'),
    path('description_provider/', ProvidingDescription.as_view(), name='description_provider')
]
     
