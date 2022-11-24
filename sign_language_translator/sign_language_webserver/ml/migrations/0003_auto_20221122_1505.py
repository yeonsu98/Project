# Generated by Django 3.2 on 2022-11-22 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_auto_20221122_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='ml_model',
            name='date_published',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='DATE_PUBLISHED'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ml_model',
            name='model_file',
            field=models.FileField(blank=True, upload_to='models/', verbose_name='MODEL_FILE'),
        ),
    ]