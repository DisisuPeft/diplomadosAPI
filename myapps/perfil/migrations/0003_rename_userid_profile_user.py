# Generated by Django 5.1.3 on 2024-11-12 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_profile_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userID',
            new_name='user',
        ),
    ]
