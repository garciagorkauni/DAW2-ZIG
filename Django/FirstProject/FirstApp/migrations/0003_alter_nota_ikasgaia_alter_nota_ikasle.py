# Generated by Django 5.1.1 on 2024-10-03 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_ikasgaia_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='ikasgaia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.ikasgaia'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='ikasle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.ikasle'),
        ),
    ]
