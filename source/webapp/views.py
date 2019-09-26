from django.shortcuts import render, get_object_or_404, redirect
# from webapp.forms import IssueForm
from webapp.models import Issue
from django.views.generic import View, TemplateView, RedirectView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context

