# Generated by Django 4.2 on 2023-05-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhammer', '0004_alter_armecontact_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campagne',
            name='campagne_etat',
            field=models.CharField(choices=[('En pause', 'En pause'), ('En cours', 'En cours'), ('Terminée', 'Terminée')], max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='alignement',
            field=models.CharField(choices=[('Chaotique', 'Chaotique'), ('Neutre', 'Neutre'), ('Bon', 'Bon'), ('Loyal', 'Loyal'), ('Mauvais', 'Mauvais')], max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='race',
            field=models.CharField(choices=[('Nain', 'Nain'), ('Halfeling', 'Halfeling'), ('Humain', 'Humain'), ('Elfe', 'Elfe')], max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='sexe',
            field=models.CharField(choices=[('Femelle', 'Femelle'), ('Mâle', 'Mâle')], max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='vocation',
            field=models.CharField(choices=[('Forestier', 'Forestier'), ('Filou', 'Filou'), ('Guerrier', 'Guerrier'), ('Erudit', 'Erudit')], max_length=50),
        ),
    ]