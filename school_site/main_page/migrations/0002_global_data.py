# Generated by Django 4.2.15 on 2024-08-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='global_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.IntegerField()),
                ('graduates', models.IntegerField()),
                ('teachers', models.IntegerField()),
                ('students', models.IntegerField()),
            ],
        ),
    ]
