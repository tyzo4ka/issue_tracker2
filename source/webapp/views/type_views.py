from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class TypeView(ListView):
    template_name = 'type/types.html'
    context_object_name = "types"
    model = Type


class TypeCreateView(LoginRequiredMixin, CreateView):
    model = Type
    template_name = "type/create_type.html"
    form_class = TypeForm

    def get_success_url(self):
        return reverse("webapp:all_types")


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = "type/type_update.html"
    context_object_name = "type"

    def get_success_url(self):
        return reverse("webapp:all_types")


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    form_class = TypeForm
    template_name = "type/type_delete.html"
    model = Type
    success_url = reverse_lazy("webapp:all_types")
    context_object_name = "type"
