# Generated by Django 3.2.7 on 2022-07-04 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaSoporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soporte', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=32)),
                ('comentario', models.TextField(blank=True)),
                ('creacion', models.DateField()),
                ('persona_soporte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='soporte.personasoporte')),
            ],
        ),
    ]
