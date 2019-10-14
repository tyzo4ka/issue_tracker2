from django.urls import reverse, reverse_lazy
from django.db.models import Q
from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    context_object_name = 'issues'
    model = Issue
    template_name = 'issue/index.html'
    ordering = ['-created_date']
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_query:
            context['query'] = urlencode({'search': self.search_query})
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_query:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_query)
                | Q(description__icontains=self.search_query)
            )
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_object_name = "issue"
    model = Issue


class IssueCreateView(CreateView):
    model = Issue
    template_name = "issue/create.html"
    form_class = IssueForm

    def get_success_url(self):
        return reverse("issue_view", kwargs={"pk": self.object.pk})


class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issue/update.html"
    context_object_name = "issue"

    def get_success_url(self):
        return reverse("issue_view", kwargs={"pk": self.object.pk})


class IssueDeleteView(DeleteView):
    form_class = IssueForm
    template_name = "issue/delete.html"
    model = Issue
    success_url = reverse_lazy("index")
    context_object_name = "issue"
