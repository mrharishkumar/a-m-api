# Generated by Django 4.1.3 on 2022-12-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetrequests', '0002_alter_assetrequest_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetrequest',
            name='status',
            field=models.CharField(choices=[('GRANTED', 'Granted'), ('DENIED', 'Denied'), ('PENDING', 'Pending'), ('RETURNED', 'Returned')], default='PENDING', max_length=10),
        ),
    ]
