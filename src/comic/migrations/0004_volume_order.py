# Generated by Django 4.0.7 on 2023-08-28 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0003_alter_project_author_alter_project_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
