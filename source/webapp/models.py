from django.db import models


class Issue(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name="Small description")
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Full description")
    status = models.ForeignKey("Status", on_delete=models.PROTECT, null=False, blank=False, verbose_name="Status")
    type = models.ForeignKey("Type", on_delete=models.PROTECT, null=False, blank=False, verbose_name="Type", related_name="issue_type")
    project = models.ForeignKey("Project", on_delete=models.PROTECT, null=True, blank=False, related_name="issues",
                                verbose_name="Project")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Time updated')


    def __str__(self):
        return self.summary


class Status(models.Model):
    state = models.CharField(max_length=20, verbose_name='state')

    def __str__(self):
        return self.state


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Project name")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Project description')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    status = models.ForeignKey("ProjectStatus", on_delete=models.PROTECT, null=True,
                               default=1)

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")

    def __str__(self):
        return self.name
