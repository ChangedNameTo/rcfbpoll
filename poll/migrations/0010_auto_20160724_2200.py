# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-24 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0009_auto_20160724_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('primary_affiliation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='primary_affiliation',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='ballot',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='usersecondaryaffiliations',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
        migrations.AddField(
            model_name='ballot',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='poll.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersecondaryaffiliations',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='poll.User'),
            preserve_default=False,
        ),
    ]