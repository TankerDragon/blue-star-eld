# Generated by Django 4.0.1 on 2022-06-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sameld', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='eld_device',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]