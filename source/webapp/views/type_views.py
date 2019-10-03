from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import TemplateView, ListView


class TypeView(TemplateView):
    template_name = 'type/types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(ListView):

    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, "type/create_type.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                name=form.cleaned_data["name"])
            return redirect("all_types")
        else:
            return render(request, "type/create_type.html", context={'form': form})


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
