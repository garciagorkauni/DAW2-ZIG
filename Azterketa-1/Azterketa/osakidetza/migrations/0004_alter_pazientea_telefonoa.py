# Generated by Django 5.1.2 on 2024-10-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osakidetza', '0003_alter_zita_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pazientea',
            name='telefonoa',
            field=models.IntegerField(max_length=10),
        ),
    ]
