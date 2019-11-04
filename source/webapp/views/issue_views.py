from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic.base import View

from webapp.forms import IssueForm
from webapp.models import Issue, Project
from accounts.models import Team
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .base import SearchView


class IndexView(SearchView):
    context_object_name = 'issues'
    model = Issue
    template_name = 'issue/index.html'
    ordering = ['-created_date']
    paginate_by = 3
    paginate_orphans = 1

    def get_query(self):
        return Q(summary__icontains=self.search_query) | Q(description__icontains=self.search_query)


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_object_name = "issue"
    model = Issue


class UserPassesCheck(View):

    def check(self, project_pk, user_name):
        project = Project.objects.filter(pk=project_pk)
        print(project)
        print(user_name)
        print(project[0].projects.all())
        teams = project[0].projects.all()
        for user in teams:
            print(user.user)
            if user_name == user.user:
                return True
            else:
                return False


class IssueCreateView(UserPassesCheck, CreateView):
    model = Issue
    template_name = "issue/create.html"
    form_class = IssueForm

    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"]

    def get_success_url(self):
        return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})


class IssueUpdateView(UserPassesCheck, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issue/update.html"
    context_object_name = "issue"

    def get(self, *args, **kwargs):
        project_pk = self.get_object().project.pk
        print(project_pk)
        check = self.check(project_pk, self.request.user)
        if check:
            return super().get(self.request)
        return HttpResponseForbidden("Access is denied")

    def get_success_url(self):
        return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})


class IssueDeleteView(UserPassesTestMixin, DeleteView):
    form_class = IssueForm
    template_name = "issue/delete.html"
    model = Issue
    success_url = reverse_lazy("webapp:index")
    context_object_name = "issue"

    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"]
