# Generated by Django 3.2.8 on 2022-02-22 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Competencies',
            new_name='Competencie',
        ),
        migrations.RenameModel(
            old_name='Experiences',
            new_name='Experience',
        ),
    ]
