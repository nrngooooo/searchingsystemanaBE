# Generated by Django 5.1.2 on 2024-12-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0003_remove_film_genres_moviegenre'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='filmImage',
            field=models.ImageField(blank=True, null=True, upload_to='film/'),
        ),
    ]
