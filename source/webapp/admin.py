from django.contrib import admin
from webapp.models import Issue, Status, Type


class IssueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'description', "status", "type", 'created_date']
    list_filter = ['status', "type"]
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'description']
    exclude = []
    readonly_fields = ['created_date']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
