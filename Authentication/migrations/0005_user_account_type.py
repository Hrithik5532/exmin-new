# Generated by Django 4.2.4 on 2024-02-03 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_rename_designation_recruiter_authorized_person_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(default='employee', max_length=20),
        ),
    ]
