# Generated by Django 3.2 on 2022-11-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ml_model',
            name='date_published',
        ),
        migrations.AddField(
            model_name='ml_model',
            name='model_file',
            field=models.FileField(blank=True, upload_to='', verbose_name='MODEL_FILE'),
        ),
    ]
