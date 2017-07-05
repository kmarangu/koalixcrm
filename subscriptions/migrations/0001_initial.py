# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Contract', verbose_name='Subscription Type')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventdate', models.DateField(blank=True, null=True, verbose_name='Event Date')),
                ('event', models.CharField(choices=[('O', 'Offered'), ('C', 'Canceled'), ('S', 'Signed')], max_length=1, verbose_name='Event')),
                ('subscriptions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.Subscription', verbose_name='Subscription')),
            ],
            options={
                'verbose_name': 'Subscription Event',
                'verbose_name_plural': 'Subscription Events',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.Product')),
                ('cancelationPeriod', models.IntegerField(blank=True, null=True, verbose_name='Cancelation Period (months)')),
                ('automaticContractExtension', models.IntegerField(blank=True, null=True, verbose_name='Automatic Contract Extension (months)')),
                ('automaticContractExtensionReminder', models.IntegerField(blank=True, null=True, verbose_name='Automatic Contract Extensoin Reminder (days)')),
                ('minimumDuration', models.IntegerField(blank=True, null=True, verbose_name='Minimum Contract Duration')),
                ('paymentIntervall', models.IntegerField(blank=True, null=True, verbose_name='Payment Intervall (days)')),
                ('contractDocument', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Contract Documents')),
            ],
            options={
                'verbose_name': 'Subscription Type',
                'verbose_name_plural': 'Subscription Types',
            },
            bases=('crm.product',),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscriptiontype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.SubscriptionType', verbose_name='Subscription Type'),
        ),
    ]
