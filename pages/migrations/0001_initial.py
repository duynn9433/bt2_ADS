# Generated by Django 4.0.2 on 2022-03-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, verbose_name='PageContent')),
            ],
        ),
    ]
