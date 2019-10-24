from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class StatusView(ListView):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    template_name = "status/create_status.html"
    form_class = StatusForm

    def get_success_url(self):
        return reverse("webapp:all_statuses")


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "status/status_update.html"
    context_object_name = "status"

    def get_success_url(self):
        return reverse("webapp:all_statuses")


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    form_class = StatusForm
    template_name = "status/status_delete.html"
    model = Status
    success_url = reverse_lazy("webapp:all_statuses")
    context_object_name = "status"
    with_confirmation = False
