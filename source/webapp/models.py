from django.db import models


class Issue(models.Model):
    summury = models.CharField(max_length=300, null=False, blank=False, verbose_name="Small description")
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Full description")
    status = models.ForeignKey("Status", on_delete=models.PROTECT, null=False, blank=False, verbose_name="Status")
    type = models.ForeignKey("Type", on_delete=models.PROTECT, null=False, blank=False, verbose_name="Type")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return self.summury


class Status(models.Model):
    state = models.CharField(max_length=20, verbose_name='state')

    def __str__(self):
        return self.state


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')

    def __str__(self):
        return self.name
