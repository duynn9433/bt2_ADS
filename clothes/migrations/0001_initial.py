# Generated by Django 4.0.2 on 2022-03-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=60)),
                ('style', models.CharField(max_length=60)),
                ('size', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='clothes.vendor')),
            ],
        ),
    ]
