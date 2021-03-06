# Generated by Django 3.2.7 on 2022-07-05 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('ciudad', models.CharField(max_length=64)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=64)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precio', models.BooleanField(default=True)),
                ('detalle', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=32)),
                ('comentario', models.TextField(blank=True)),
                ('creacion', models.DateField()),
                ('nombre_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura.cliente')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura.productos')),
            ],
        ),
    ]
