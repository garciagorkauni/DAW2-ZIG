# Generated by Django 5.1.2 on 2024-10-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medikua',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('izena', models.CharField(max_length=75)),
                ('abizena', models.CharField(max_length=75)),
                ('espezialidadea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pazientea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('izena', models.CharField(max_length=75)),
                ('abizena', models.CharField(max_length=75)),
                ('telefonoa', models.CharField(max_length=10)),
            ],
        ),
    ]
