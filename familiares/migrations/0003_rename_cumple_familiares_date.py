# Generated by Django 4.0.4 on 2022-05-29 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_familiares_cumple'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiares',
            old_name='cumple',
            new_name='date',
        ),
    ]