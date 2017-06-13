# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siad', '0009_auto_20170525_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidoPaterno', models.CharField(max_length=20)),
                ('apellidoMaterno', models.CharField(max_length=20)),
                ('fechaCreacionRegistro', models.DateField(default=django.utils.timezone.now)),
                ('formaContacto', models.CharField(choices=[('Personal', 'Personal'), ('Telefono', 'Telefono'), ('Correo elctronico', 'Correo electronico'), ('Otro', 'Otro')], default='Personal', max_length=20)),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=13)),
                ('medioContacto', models.CharField(choices=[('Recomendacion', 'Recomendacion'), ('Instalaciones', 'Instalaciones'), ('Internet', 'Internet'), ('Lona publicitaria', 'Lona publiciataria'), ('Volante', 'volante'), ('Radio', 'Radio'), ('Otro', 'Otro')], default='Recomendacion', max_length=20)),
                ('plantel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siad.Plantel')),
                ('promotor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siad.Empleado')),
                ('servicioInteres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siad.Curso')),
            ],
            options={
                'ordering': ['apellidoPaterno'],
            },
        ),
    ]