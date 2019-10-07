from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import IssueForm
from webapp.models import Issue
from django.views.generic import View, ListView, DetailView, CreateView


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

    # def get(self, request, *args, **kwargs):
    #     pk = kwargs.get(self.key_kwarg)
    #     issue = get_object_or_404(self.model, pk=pk)
    #     form = IssueForm(data={
    #         'summary': issue.summary,
    #         'description': issue.description,
    #         'status': issue.status,
    #         'type': issue.type
    #     })
    #     return render(request, 'Issue/update.html', context={
    #         'form': form,
    #         'issue': issue
    #     })

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwargs)
        context_object_name = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=context_object_name, data=request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid()
        else:
            return self.form_invalid(form, context_object_name)
        # form = IssueForm(data=request.POST)
        # issue_pk = kwargs.get('pk')
        # issue = get_object_or_404(Issue, pk=issue_pk)
        # if form.is_valid():
        #     issue.summary = form.cleaned_data['summary']
        #     issue.description = form.cleaned_data['description']
        #     issue.status = form.cleaned_data['status']
        #     issue.type = form.cleaned_data['type']
        #     issue.save()
        #     return redirect("issue_view", pk=issue.pk)
        # else:
        #     return render(request, "Issue/update.html", context={"form": form, "issue": issue})

    def form_valid(self):
        # self.object = self.model.objects.create(**form.cleaned_data)
        return redirect(self.get_redirect_url())

    def form_invalid(self, form, context_object_name):
        context = {'form': form, self.object_name: context_object_name}
        return render(self.request, self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url
