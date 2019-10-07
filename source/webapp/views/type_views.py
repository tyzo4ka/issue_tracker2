from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.forms import TypeForm
from webapp.models import Type
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


class TypeUpdateView(ListView):

    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'name': type.name})
        return render(request, 'type/type_update.html', context={
            'form': form,
            'type': type
        })

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        if form.is_valid():
            type.name = form.cleaned_data['name']
            type.save()
            return redirect("all_types")
        else:
            return render(request, "Issue/update.html", context={"form": form, "type": type})


class TypeDeleteView(ListView):
    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        return render(request, "type/type_delete.html", context={"type": type})

    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        type.delete()
        return redirect("all_types")
