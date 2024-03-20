# Generated by Django 4.1.13 on 2024-03-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименонивания блюда')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.CharField(max_length=500, verbose_name='Ссылка на фото')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
    ]
