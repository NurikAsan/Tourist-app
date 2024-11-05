from django.urls import path
from .views import RegisterView, AuthenticationUserView, VerifyOtpView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('authenticate/', AuthenticationUserView.as_view()),
    path('verify-otp/', VerifyOtpView.as_view())
]
