# Generated by Django 4.1 on 2024-07-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=10)),
                ('uniform_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
