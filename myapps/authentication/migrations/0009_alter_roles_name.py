# Generated by Django 5.1.3 on 2024-11-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_usercustomize_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
