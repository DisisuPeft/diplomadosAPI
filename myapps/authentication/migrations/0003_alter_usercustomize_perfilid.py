# Generated by Django 5.1.3 on 2024-11-12 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
        ('perfil', '0002_alter_profile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomize',
            name='perfilID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_customize', to='perfil.profile'),
        ),
    ]
