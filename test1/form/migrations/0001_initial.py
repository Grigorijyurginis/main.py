# Generated by Django 4.1.1 on 2022-09-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('sourname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('age', models.DateField(verbose_name='Дата рождения')),
                ('comment', models.TextField(verbose_name='О себе')),
            ],
        ),
    ]
