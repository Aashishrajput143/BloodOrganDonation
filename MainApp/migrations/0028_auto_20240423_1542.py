# Generated by Django 3.0.5 on 2024-04-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0027_auto_20240422_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='web',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='web',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
