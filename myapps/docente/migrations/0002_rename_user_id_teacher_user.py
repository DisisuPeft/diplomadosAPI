# Generated by Django 5.1.3 on 2024-12-10 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='user_id',
            new_name='user',
        ),
    ]
