# Generated by Django 4.2.4 on 2024-02-07 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_jobpositions_functional_area_and_more'),
        ('Dashboard', '0005_alter_functionalarea_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FunctionalArea',
        ),
        migrations.DeleteModel(
            name='IndustryType',
        ),
    ]