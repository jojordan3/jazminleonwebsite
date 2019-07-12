from .views import *
from django.urls import path


urlpatterns = [
    path('terms-of-use/', TermsOfUse.as_view()),
    path('privacy-policy/', PrivacyPolicy.as_view()),
]