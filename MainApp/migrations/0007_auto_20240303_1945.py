# Generated by Django 3.0.5 on 2024-03-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20240303_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
