# Generated by Django 2.1.5 on 2019-04-27 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_etudiant_ecole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='cne',
        ),
    ]
