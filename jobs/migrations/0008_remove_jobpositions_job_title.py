# Generated by Django 4.2.4 on 2024-02-08 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_jobpositions_functional_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpositions',
            name='job_title',
        ),
    ]
