# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-11-20 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTemperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentUID', models.CharField(max_length=200)),
                ('TemperatureMeasurdDate', models.DateField()),
                ('TemperatureMeasurd', models.FloatField()),
                ('SymptomsOfCold', models.CharField(max_length=5)),
                ('NoteInfo', models.CharField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='PersonnelList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonnelNameID', models.CharField(max_length=20)),
                ('PersonnelName', models.CharField(max_length=20)),
                ('Affiliation', models.CharField(max_length=40)),
                ('values', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ElementarySchoolID', models.CharField(max_length=20)),
                ('Grage', models.IntegerField()),
                ('ClaseNo', models.IntegerField()),
                ('StudentID', models.IntegerField()),
                ('StudentName', models.CharField(max_length=30)),
                ('LoginEmail', models.EmailField(max_length=254)),
            ],
        ),
    ]
