# Generated by Django 3.2.4 on 2021-06-27 00:00

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210626_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petprofile',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=150, null=True, upload_to=data.models.get_upload_path),
        ),
    ]
