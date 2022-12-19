# Generated by Django 4.1.3 on 2022-12-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_alter_asset_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.CharField(default='AVAILABLE', max_length=15),
        ),
        migrations.AlterField(
            model_name='asset',
            name='image_url',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]