# Generated by Django 4.0.7 on 2023-08-22 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('accounts', '0005_delete_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.imagecontent'),
        ),
    ]