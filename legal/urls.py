from django.urls import include, path, re_path
from django.template.loader import render


urls = [
    path('privacy-policy/', render('privacy.html'), name='privacy_policy'),
    path('terms-of-use/', render('terms.html'), name='terms_of_use'),
]