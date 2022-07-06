# Generated by Django 3.2.7 on 2022-07-06 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('ciudad', models.CharField(max_length=64)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=45)),
            ],
        ),
    ]
