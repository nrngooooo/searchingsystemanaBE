# Generated by Django 5.1.2 on 2024-12-02 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='cast',
        ),
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AlterField(
            model_name='people',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='FilmRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('actor', 'Actor'), ('director', 'Director'), ('producer', 'Producer'), ('writer', 'Writer')], max_length=50)),
                ('role_name', models.CharField(blank=True, max_length=255, null=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='dataApp.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_roles', to='dataApp.people')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(related_name='films', to='dataApp.genre'),
        ),
    ]
