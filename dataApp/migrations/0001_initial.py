# Generated by Django 5.1.2 on 2024-11-15 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('event_description', models.TextField()),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Occupations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=255)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('biography', models.TextField()),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('albumImage', models.ImageField(blank=True, null=True, upload_to='album/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music_albums', to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('synopsis', models.TextField()),
                ('cast', models.ManyToManyField(related_name='films', to='dataApp.people')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directed_films', to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creation_date', models.DateField()),
                ('artImage', models.ImageField(blank=True, null=True, upload_to='art/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='Aliases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias_name', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.categories')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.events')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleOccupations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.occupations')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_type', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='dataApp.people')),
                ('related_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_person', to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=255)),
                ('search_date', models.DateTimeField(auto_now_add=True)),
                ('result_count', models.IntegerField()),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('profile_url', models.URLField(max_length=500)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=255)),
                ('source_url', models.URLField(max_length=500)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataApp.people')),
            ],
        ),
    ]