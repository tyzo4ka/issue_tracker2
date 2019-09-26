from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=300, required=True, label="Summary")
    description = forms.CharField(max_length=5000, required=True, label="Description", widget=widgets.Textarea)
    status = forms.ModelChoiceField(to_field_name='state', queryset=Status.objects.all(), required=True, label="Status",
                                    empty_label=None)
    type = forms.ModelChoiceField(to_field_name="name", queryset=Type.objects.all(), required=True, label="Type",
                                  empty_label=None)


class StatusForm(forms.Form):
    state = forms.CharField(max_length=100, required=True, label="state")


class TypeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="name")
