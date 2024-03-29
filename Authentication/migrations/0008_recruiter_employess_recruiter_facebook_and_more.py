# Generated by Django 5.0.1 on 2024-02-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_alter_user_city_alter_user_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='employess',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='map_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='wesbsite',
            field=models.URLField(blank=True, null=True),
        ),
    ]
