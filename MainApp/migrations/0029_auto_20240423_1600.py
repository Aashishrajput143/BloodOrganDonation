# Generated by Django 3.0.5 on 2024-04-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0028_auto_20240423_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='web',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='web',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
