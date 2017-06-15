# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroRegistro', models.IntegerField()),
                ('concepto', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fecha', models.DateField()),
                ('factura', models.BooleanField()),
                ('montoCubierto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esquema', models.CharField(choices=[(b'Semanal', b'Semanal'), (b'Quincenal', b'Quincenal'), (b'Mensual', b'Mensual'), (b'Un solo pago', b'Un solo pago'), (b'Otro', b'otro')], default=b'Semanal', max_length=10)),
                ('fechaInicio', models.DateTimeField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
