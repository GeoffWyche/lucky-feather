# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_text', models.CharField(max_length=200)),
                ('is_animal', models.BooleanField(default=False)),
                ('no_link', models.ForeignKey(to='animals.TreeNode', related_name='no_ans')),
                ('yes_link', models.ForeignKey(to='animals.TreeNode', related_name='yes_ans')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
