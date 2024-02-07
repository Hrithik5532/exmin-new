# Generated by Django 4.2.4 on 2024-02-07 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0011_rename_employess_recruiter_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='additional_qualification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_mn_experience',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_position',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_yr_experience',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='exim_mn_experience',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='exim_yr_experience',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_employer',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='passing_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='employee-profile'),
        ),
        migrations.AddField(
            model_name='employee',
            name='resume',
            field=models.ImageField(blank=True, null=True, upload_to='employee-resume'),
        ),
        migrations.AddField(
            model_name='employee',
            name='specialised',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nearest_station',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='FunctionalArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.industrytype')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='current_industry',
            field=models.ManyToManyField(to='Authentication.industrytype'),
        ),
        migrations.AddField(
            model_name='employee',
            name='funtional_area',
            field=models.ManyToManyField(to='Authentication.functionalarea'),
        ),
    ]
