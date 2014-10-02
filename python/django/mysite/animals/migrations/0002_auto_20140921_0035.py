# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treenode',
            name='no_link',
            field=models.ForeignKey(related_name='no_ans', null=True, to='animals.TreeNode'),
        ),
        migrations.AlterField(
            model_name='treenode',
            name='yes_link',
            field=models.ForeignKey(related_name='yes_ans', null=True, to='animals.TreeNode'),
        ),
    ]
