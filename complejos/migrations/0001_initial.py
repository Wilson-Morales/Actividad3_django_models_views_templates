# Generated by Django 4.0.5 on 2022-07-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estadios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('num_camerinos', models.IntegerField()),
                ('num_marcadores', models.IntegerField()),
                ('num_cabinas_radio', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('num_monumentos', models.IntegerField()),
            ],
        ),
    ]
