# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=50, verbose_name='UF')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Bairro')),
                ('street', models.CharField(max_length=50, verbose_name='Rua')),
                ('block', models.CharField(max_length=50, verbose_name='Conjunto')),
                ('number', models.CharField(max_length=10, verbose_name='Numero')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_user', models.CharField(max_length=150, unique=True, verbose_name='ID de usuário')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='Email do usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Staff')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.staff', models.Model),
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Staff')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.staff', models.Model),
        ),
    ]
