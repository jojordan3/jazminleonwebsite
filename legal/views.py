from django.views.generic import TemplateView


class PrivacyPolicy(TemplateView):
    template_name = 'privacy.html'


class TermsOfUse(TemplateView):
    template_name = 'terms.html'