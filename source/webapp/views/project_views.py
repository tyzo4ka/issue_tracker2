from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm
from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/projects.html'
    ordering = ['-created_date']


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    context_object_name = "project"
    model = Project


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
