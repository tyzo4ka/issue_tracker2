from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import IssueForm
from webapp.models import Issue
from .base import UpdateView
from django.views.generic import ListView, DetailView, CreateView


class IndexView(ListView):
    context_object_name = 'issues'
    model = Issue
    template_name = 'Issue/index.html'
    ordering = ['-created_date']
    paginate_by = 3
    paginate_orphans = 1


class IssueView(DetailView):
    template_name = 'Issue/issue.html'
    context_object_name = "issue"
    model = Issue


class IssueCreateView(CreateView):
    model = Issue
    template_name = "Issue/create.html"
    form_class = IssueForm


    def get_success_url(self):
        return reverse("issue_view", kwargs={"pk": self.object.pk})


class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "Issue/update.html"
    object_name = "issue"

    def get_redirect_url(self):
        return reverse("issue_view", kwargs={"pk": self.object.pk})


    # def get(self, request, *args, **kwargs):
    #     issue_pk = kwargs.get('pk')
    #     issue = get_object_or_404(Issue, pk=issue_pk)
    #     form = IssueForm(data={
    #         'summary': issue.summary,
    #         'description': issue.description,
    #         'status': issue.status,
    #         'type': issue.type
    #     })
    #     return render(request, 'Issue/update.html', context={
    #         'form': form,
    #         'issue': issue
    #     })
    #
    # def post(self, request, *args, **kwargs):
    #     form = IssueForm(data=request.POST)
    #     issue_pk = kwargs.get('pk')
    #     issue = get_object_or_404(Issue, pk=issue_pk)
    #     if form.is_valid():
    #         issue.summary = form.cleaned_data['summary']
    #         issue.description = form.cleaned_data['description']
    #         issue.status = form.cleaned_data['status']
    #         issue.type = form.cleaned_data['type']
    #         issue.save()
    #         return redirect("issue_view", pk=issue.pk)
    #     else:
    #         return render(request, "Issue/update.html", context={"form": form, "issue": issue})
    #

class IssueDeleteView(ListView):
    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        return render(request, "Issue/delete.html", context={"issue": issue})

    def post(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        issue.delete()
        return redirect("index")