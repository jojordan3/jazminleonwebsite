from .views import *
from django.urls import path


urlpatterns = [
    ('terms-of-use/', terms_of_use),
    ('privacy-policy/', privacy_policy),
]