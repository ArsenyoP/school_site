# Generated by Django 4.2.15 on 2024-08-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='image',
            field=models.ImageField(default='', upload_to='teachers_images'),
        ),
    ]
