# Generated by Django 4.0.7 on 2023-12-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_featureflag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureflag',
            name='value',
            field=models.BooleanField(default=False, verbose_name='Feature Enabled'),
        ),
    ]