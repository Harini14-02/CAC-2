# Generated by Django 4.2.7 on 2024-01-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('activity', models.TextField(max_length=250)),
                ('destination', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
