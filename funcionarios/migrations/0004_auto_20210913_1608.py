# Generated by Django 3.2.7 on 2021-09-13 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20210913_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administradores',
            old_name='cpf',
            new_name='CPF',
        ),
        migrations.RenameField(
            model_name='administradores',
            old_name='phone',
            new_name='telefone',
        ),
    ]