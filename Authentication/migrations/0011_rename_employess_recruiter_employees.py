# Generated by Django 5.0.1 on 2024-02-05 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0010_rename_wesbsite_recruiter_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiter',
            old_name='employess',
            new_name='employees',
        ),
    ]
