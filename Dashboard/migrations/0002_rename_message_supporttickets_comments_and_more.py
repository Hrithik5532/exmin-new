# Generated by Django 5.0.1 on 2024-02-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supporttickets',
            old_name='message',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='supporttickets',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='supporttickets',
            name='resolved',
        ),
        migrations.AddField(
            model_name='supporttickets',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
