from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView


class StatusView(ListView):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    model = Status
    template_name = "status/create_status.html"
    form_class = StatusForm

    def get_success_url(self):
        return reverse("all_statuses")


class StatusUpdateView(ListView):

    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data={
            'state': status.state})
        return render(request, 'status/status_update.html', context={
            'form': form,
            'status': status
        })

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        if form.is_valid():
            status.state = form.cleaned_data['state']
            status.save()
            return redirect("all_statuses")
        else:
            return render(request, "status/status_update.html", context={"form": form, "status": status})


class StatusDeleteView(ListView):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        return render(request, "status/status_delete.html", context={"status": status})

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        status.delete()
        return redirect("all_statuses")
