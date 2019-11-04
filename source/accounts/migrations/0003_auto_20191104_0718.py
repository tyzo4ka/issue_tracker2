# Generated by Django 2.2.5 on 2019-11-04 07:18

from django.db import migrations

def create_profiles(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Profile = apps.get_model("accounts", "Profile")
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)


def drop_profiles(apps, schema_editor):
    Profile = apps.get_model("accounts", "Profile")
    Profile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191104_0436'),
    ]

    operations = [
        migrations.RunPython(create_profiles, drop_profiles),
    ]
