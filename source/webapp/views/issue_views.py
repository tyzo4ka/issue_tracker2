from django.urls import reverse
from webapp.forms import IssueForm
from webapp.models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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
    context_object_name = "issue"

    def get_success_url(self):
        return reverse("issue_view", kwargs={"pk": self.object.pk})


class IssueDeleteView(DeleteView):
    form_class = IssueForm
    template_name = "Issue/delete.html"
    model = Issue
    redirect_url = "index"
    object_name = "issue"
