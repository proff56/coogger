# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-21 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0005_auto_20171018_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField()),
                ('ip', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0, verbose_name='görüntülenme sayısı'),
        ),
        migrations.AlterField(
            model_name='userfollow',
            name='user',
            field=models.CharField(choices=[('coogger', 'coogger'), ('hakancelik', 'hakancelik'), ('ibrahimsmngl', 'ibrahimsmngl'), ('ufukozer', 'ufukozer'), ('baristutakli', 'baristutakli'), ('imerafera', 'imerafera'), ('fadimekaplan', 'fadimekaplan'), ('vayra53', 'vayra53'), ('teibe', 'teibe'), ('ooznur', 'ooznur'), ('arslan', 'arslan'), ('saiddemir', 'saiddemir'), ('dersim67', 'dersim67')], max_length=37),
        ),
    ]