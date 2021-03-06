# Generated by Django 3.2.9 on 2021-12-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pajaro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=40)),
                ('zona', models.CharField(max_length=40)),
                ('esExotico', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('esCastrado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=40)),
                ('deAguaSalada', models.BooleanField(null=True)),
            ],
        ),
    ]
