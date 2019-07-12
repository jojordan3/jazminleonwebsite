from .views import *
from django.urls import path


urlpatterns = [
    ('terms-of-use/', TermsOfUse.as_view()),
    ('privacy-policy/', PrivacyPolicy.as_view()),
]