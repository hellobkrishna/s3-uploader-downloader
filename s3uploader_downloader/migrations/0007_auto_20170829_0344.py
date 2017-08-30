# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s3uploader_downloader', '0006_auto_20170828_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploadandurl',
            name='folder_name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
