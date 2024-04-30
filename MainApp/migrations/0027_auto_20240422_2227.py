# Generated by Django 3.0.5 on 2024-04-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0026_auto_20240422_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='details',
            new_name='details1',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='terms',
            new_name='details2',
        ),
        migrations.RenameField(
            model_name='rewards',
            old_name='details',
            new_name='details1',
        ),
        migrations.RenameField(
            model_name='rewards',
            old_name='terms',
            new_name='details2',
        ),
        migrations.AddField(
            model_name='offer',
            name='details3',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='details4',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='details5',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='terms1',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='terms2',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='terms3',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='terms4',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='terms5',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='details3',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='details4',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='details5',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='terms1',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='terms2',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='terms3',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='terms4',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='rewards',
            name='terms5',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]