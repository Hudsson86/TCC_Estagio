# Generated by Django 4.0 on 2021-12-11 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vagas',
            new_name='Vaga',
        ),
        migrations.AlterModelOptions(
            name='vaga',
            options={'ordering': ('-created',)},
        ),
    ]
