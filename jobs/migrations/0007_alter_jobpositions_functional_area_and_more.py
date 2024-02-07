# Generated by Django 4.2.4 on 2024-02-07 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0012_industrytype_employee_additional_qualification_and_more'),
        ('jobs', '0006_jobapplications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpositions',
            name='functional_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.functionalarea'),
        ),
        migrations.AlterField(
            model_name='jobpositions',
            name='industry_type',
            field=models.ManyToManyField(to='Authentication.industrytype'),
        ),
    ]