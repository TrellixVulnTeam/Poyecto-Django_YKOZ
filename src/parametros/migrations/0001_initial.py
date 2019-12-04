# Generated by Django 2.2.6 on 2019-10-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstaCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEsCi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreEtni', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo De Logro',
                'verbose_name_plural': 'Tipo De Logros',
            },
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTiDo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTiEs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLogr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTiLo', models.CharField(max_length=50)),
            ],
        ),
    ]
