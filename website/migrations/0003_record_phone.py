# Generated by Django 4.2.6 on 2023-10-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_record_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='phone',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]
