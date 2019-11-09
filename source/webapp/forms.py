from django import forms
from webapp.models import Issue, Status, Type, Project, User


class IssueForm(forms.ModelForm):

    def __init__(self, **kwargs):
        self.projects = kwargs.pop('projects')
        print("Self projects", self.projects)
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(teams__project__in=self.projects)

    class Meta:
        model = Issue
        exclude = ["created_date", "updated_at", "created_by"]


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["state"]


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["name"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_date', 'updated_date']


class ProjectIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["summary", "description"]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Find")


