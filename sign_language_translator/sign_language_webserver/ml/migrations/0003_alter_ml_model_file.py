# Generated by Django 3.2 on 2022-11-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_ml_model_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml_model',
            name='file',
            field=models.FileField(blank=True, upload_to='models/'),
        ),
    ]