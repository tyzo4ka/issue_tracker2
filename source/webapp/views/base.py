# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import View
#
#
# class UpdateView(View):
#     form_class = None
#     template_name = None
#     key_kwargs = "pk"
#     model = None
#     redirect_url = None
#     object_name = "object"
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get(self.key_kwargs)
#         context_object_name = get_object_or_404(self.model, pk=pk)
#         form = self.form_class(instance=context_object_name)
#         context = {"form": form,
#                    self.object_name: context_object_name}
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         pk = kwargs.get(self.key_kwargs)
#         context_object_name = get_object_or_404(self.model, pk=pk)
#         form = self.form_class(instance=context_object_name, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return self.form_valid()
#         else:
#             return self.form_invalid(form, context_object_name)
#
#     def form_valid(self):
#         return redirect(self.get_redirect_url())
#
#     def form_invalid(self, form, context_object_name):
#         context = {'form': form, self.object_name: context_object_name}
#         return render(self.request, self.template_name, context)
#
#     def get_redirect_url(self):
#         return self.redirect_url
#
#
# class DeleteView(View):
#     form_class = None
#     template_name = None
#     key_kwargs = "pk"
#     model = None
#     redirect_url = None
#     object_name = "object"
#     with_confirmation = True
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get(self.key_kwargs)
#         context_object_name = get_object_or_404(self.model, pk=pk)
#         if self.with_confirmation:
#             return render(request, self.template_name, context={self.object_name: context_object_name})
#         else:
#             context_object_name.delete()
#             return redirect(self.redirect_url)
#
#     def post(self, request, *args, **kwargs):
#         pk = kwargs.get(self.key_kwargs)
#         context_object_name = get_object_or_404(self.model, pk=pk)
#         context_object_name.delete()
#         return redirect(self.redirect_url)


from django.urls import reverse, reverse_lazy
from django.db.models import Q
from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class SearchView(ListView):

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
                self.get_query())
        return queryset

    def get_query(self):
        return Q(name__icontains=self.search_query)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

