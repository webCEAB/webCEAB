# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-23 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_registro', models.IntegerField()),
                ('concepto', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fecha', models.DateField()),
                ('factura', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esquema', models.CharField(choices=[(b'Semanal', b'Semanal'), (b'Quincenal', b'Quincenal'), (b'Mensual', b'Mensual'), (b'Un solo pago', b'Un solo pago'), (b'Otro', b'otro')], default=b'Semanal', max_length=10)),
                ('fecha_inicio', models.DateTimeField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=100)),
                ('colonia', models.CharField(max_length=100)),
                ('ciudad_y_estado', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=50)),
                ('telefono_extension', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.AddField(
            model_name='egreso',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Proveedor'),
        ),
    ]
