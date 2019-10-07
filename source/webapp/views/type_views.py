from django.shortcuts import reverse
from webapp.forms import TypeForm
from webapp.models import Type
from .base import UpdateView, DeleteView
from django.views.generic import ListView, CreateView


class TypeView(ListView):
    template_name = 'type/types.html'
    context_object_name = "types"
    model = Type


class TypeCreateView(CreateView):
    model = Type
    template_name = "type/create_type.html"
    form_class = TypeForm

    def get_success_url(self):
        return reverse("all_types")


class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = "type/type_update.html"
    object_name = "type"

    def get_redirect_url(self):
        return reverse("all_types")


class TypeDeleteView(DeleteView):
    form_class = TypeForm
    template_name = "type/type_delete.html"
    model = Type
    redirect_url = "all_types"
    object_name = "type"
