# Generated by Django 4.2.4 on 2024-02-04 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_jobpositions_functional_area_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpositions',
            old_name='min_experience',
            new_name='experience',
        ),
    ]
