# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('ip_addr', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField(max_length=6)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('cus_ip', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=20, unique=True)),
                ('invoice_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=20)),
                ('ref_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=200)),
                ('product_status', models.CharField(max_length=20)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_id_product', to='myshop.Brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_id_product', to='myshop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='order_id_order_details', serialize=False, to='myshop.Order')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='invoice_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_no_payment', to='myshop.Order', to_field='invoice_no'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id_payment', to='myshop.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.Customer'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='invoice_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_no_order_details', to='myshop.Order', to_field='invoice_no'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_status_order_details', to='myshop.Order', to_field='order_status'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id_order_details', to='myshop.Product'),
        ),
    ]
