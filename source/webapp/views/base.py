from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View


class UpdateView(View):
    form_class = None
    template_name = None
    key_kwargs = "pk"
    model = None
    redirect_url = None
    object_name = "object"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwargs)
        context_object_name = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=context_object_name)
        context = {"form": form,
                   self.object_name: context_object_name}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwargs)
        context_object_name = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=context_object_name, data=request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid()
        else:
            return self.form_invalid(form, context_object_name)

    def form_valid(self):
        return redirect(self.get_redirect_url())

    def form_invalid(self, form, context_object_name):
        context = {'form': form, self.object_name: context_object_name}
        return render(self.request, self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    form_class = None
    template_name = None
    key_kwargs = "pk"
    model = None
    redirect_url = None
    object_name = "object"
    with_confirmation = True

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwargs)
        context_object_name = get_object_or_404(self.model, pk=pk)
        if self.with_confirmation:
            return render(request, self.template_name, context={self.object_name: context_object_name})
        else:
            context_object_name.delete()
            return redirect(self.redirect_url)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwargs)
        context_object_name = get_object_or_404(self.model, pk=pk)
        context_object_name.delete()
        return redirect(self.redirect_url)
