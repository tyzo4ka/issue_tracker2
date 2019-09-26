from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import IssueForm, StatusForm, TypeForm
from webapp.models import Issue, Status, Type
from django.views.generic import View, TemplateView, RedirectView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['issue'] = get_object_or_404(Issue, pk=issue_pk)
        return context


class IssueCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, "create.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data["summary"],
                description=form.cleaned_data["description"],
                status=form.cleaned_data["status"],
                type=form.cleaned_data['type'])
            return redirect("issue_view", pk=issue.pk)
        else:
            return render(request, "create.html", context={'form': form})


class IssueUpdateView(TemplateView):

    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type
        })
        return render(request, 'update.html', context={
            'form': form,
            'issue': issue
        })

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type = form.cleaned_data['type']
            issue.save()
            return redirect("issue_view", pk=issue.pk)
        else:
            return render(request, "update.html", context={"form": form, "issue": issue})


class IssueDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        return render(request, "delete.html", context={"issue": issue})

    def post(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        issue.delete()
        return redirect("index")


class StatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, "create_status.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                state=form.cleaned_data["state"])
            return redirect("all_statuses")
        else:
            return render(request, "create_status.html", context={'form': form})


class TypeView(TemplateView):
    template_name = 'types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, "create_type.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                name=form.cleaned_data["name"])
            return redirect("all_types")
        else:
            return render(request, "create_type.html", context={'form': form})

