# Generated by Django 4.1.7 on 2023-03-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True


operations = [


    migrations.CreateModel(
        name='registros',
        fields=[
            ('id_usuario', models.AutoField(primary_key=True)),
            ('nome', models.TextField(max_length=255)),
            ('idade', models.IntegerField()),
        ],
    ),
]
