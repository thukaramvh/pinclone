# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('pin_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('like_count', models.IntegerField()),
                ('link', models.URLField()),
                ('title', models.CharField(blank=True, max_length=128)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Pinner',
            fields=[
                ('pinner_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.URLField(blank=True)),
                ('full_name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest.Pin'),
        ),
        migrations.AddField(
            model_name='board',
            name='pinner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest.Pinner'),
        ),
    ]
