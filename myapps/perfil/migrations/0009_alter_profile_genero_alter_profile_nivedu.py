# Generated by Django 5.1.3 on 2025-03-24 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0008_genero_niveleducativo_alter_profile_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.genero'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nivEdu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.niveleducativo'),
        ),
    ]
