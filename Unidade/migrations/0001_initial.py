# Generated by Django 3.2.4 on 2021-06-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_unidade', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
            ],
        ),
    ]
