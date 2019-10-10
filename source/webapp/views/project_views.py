from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm, ProjectIssueForm
from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator


class ProjectView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/projects.html'
    ordering = ['created_date']
    paginate_by = 5
    paginate_orphans = 1


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
