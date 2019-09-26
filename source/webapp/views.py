from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import IssueForm
from webapp.models import Issue
from django.views.generic import View, TemplateView, RedirectView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['issue'] = get_object_or_404(Issue, pk=issue_pk)
        return context


class IssueUpdateView(TemplateView):

    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type
        })
        return render(request, 'update.html', context={
            'form': form,
            'issue': issue
        })

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type = form.cleaned_data['type']
            issue.save()
            return redirect("article_view", pk=issue.pk)
        else:
            return render(request, "update.html", context={"form": form, "issue": issue})

