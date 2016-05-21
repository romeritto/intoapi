# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 19:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed'), ('IO', 'Invite Only'), ('IN', 'Invisible')], default='IN', max_length=2)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
                ('facebook_share_img_url', models.URLField(blank=True, default='')),
                ('ticketshop_url', models.URLField(blank=True, default='')),
                ('sold_out', models.BooleanField(default=False)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('RE', 'Reserved'), ('TO', 'Timed out'), ('PP', 'Prending payment'), ('CA', 'Cancelled'), ('VA', 'Valid'), ('US', 'Used'), ('RV', 'Revoked')], default='PE', max_length=2)),
                ('first_use_time', models.DateTimeField(blank=True, null=True)),
                ('barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('event_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.EventProduct')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Guest')),
            ],
        ),
    ]