# Generated by Django 5.1 on 2024-11-02 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=255)),
                ('nombre', models.TextField(max_length=255)),
                ('genero', models.TextField(max_length=255)),
                ('clasificacion', models.TextField(max_length=100)),
                ('duracion', models.PositiveIntegerField()),
                ('resena', models.TextField(max_length=255)),
                ('sala', models.PositiveIntegerField()),
                ('fecha_exhibicion', models.DateField()),
                ('hora_exhibicion', models.TimeField()),
                ('valor_ticket', models.PositiveIntegerField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]