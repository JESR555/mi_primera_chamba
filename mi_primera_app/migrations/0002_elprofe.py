# Generated by Django 5.0.2 on 2024-03-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_primera_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElProfe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]