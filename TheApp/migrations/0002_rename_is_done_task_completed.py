# Generated by Django 4.2 on 2023-06-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_done',
            new_name='completed',
        ),
    ]
