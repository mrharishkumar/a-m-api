# Generated by Django 4.1.3 on 2022-12-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_alter_asset_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(default='AVAILABLE', max_length=15),
        ),
    ]