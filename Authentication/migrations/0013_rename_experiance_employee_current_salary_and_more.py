# Generated by Django 4.2.4 on 2024-02-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0012_industrytype_employee_additional_qualification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='experiance',
            new_name='current_salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='operational_area',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='shipment_expertise',
            field=models.TextField(blank=True, null=True),
        ),
    ]
