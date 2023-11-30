# Generated by Django 4.2.7 on 2023-11-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('tema', models.CharField(max_length=30)),
                ('data_cadastro', models.DateField()),
                ('emprestado', models.BooleanField(default=False)),
                ('nome_emprestado', models.CharField(max_length=50)),
                ('data_emprestimo', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField()),
                ('tempo_duracao', models.DateField()),
            ],
        ),
    ]