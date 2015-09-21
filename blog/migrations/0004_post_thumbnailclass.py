# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150920_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnailClass',
            field=models.CharField(max_length=1, default=1),
            preserve_default=False,
        ),
    ]
