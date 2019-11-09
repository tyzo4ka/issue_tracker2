from django.contrib import admin
from webapp.models import Issue, Status, Type, Project, ProjectStatus


class IssueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'description', "status", "type", 'created_date', 'assigned_to', 'created_by']
    list_filter = ['status', "type"]
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', "status", "type"]
    readonly_fields = ['created_date']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
admin.site.register(ProjectStatus)
