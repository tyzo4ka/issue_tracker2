from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm, ProjectIssueForm
from webapp.models import Project
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .base import SearchView


class ProjectView(SearchView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/projects.html'
    ordering = ['created_date']
    paginate_by = 5
    paginate_orphans = 1

    def qet_query(self):
        return Q(name__icontains=self.search_query)


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    context_object_name = "project"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectIssueForm()
        issues = context['project'].issues.order_by("-created_date")
        self.paginate_issues_to_context(issues, context)
        return context

    def paginate_issues_to_context(self, issues, context):
        paginator = Paginator(issues, 5, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['issues'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ProjectCreateView(CreateView):
    model = Project
    template_name = "project/create_project.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project_view", kwargs={"pk": self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/update_project.html"
    context_object_name = "project"

    def get_success_url(self):
        return reverse("project_view", kwargs={"pk": self.object.pk})


class ProjectDeleteView(DeleteView):
    form_class = ProjectForm
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy("all_projects")
    context_object_name = "project"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(data=request.POST)
        success_url = self.get_success_url()
        self.object.status.pk = 2
        self.object.save()

        return HttpResponseRedirect(success_url)


