from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField()
    profileImage = models.ImageField(upload_to='profile/', blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
class Art(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    artist = models.ForeignKey(People, on_delete=models.CASCADE, related_name="artworks")
    creation_date = models.DateField()
    artImage = models.ImageField(upload_to='art/', blank=True, null=True)

    def __str__(self):
        return self.title

class MusicAlbum(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    artist = models.ForeignKey(People, on_delete=models.CASCADE, related_name="music_albums")  # Link to artist in People table
    release_date = models.DateField()
    genre = models.CharField(max_length=255, null=True, blank=True)
    albumImage = models.ImageField(upload_to='album/', blank=True, null=True)

    def __str__(self):
        return self.title

class Film(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    director = models.ForeignKey(People, on_delete=models.SET_NULL, null=True, blank=True, related_name="directed_films")
    release_date = models.DateField()
    genre = models.CharField(max_length=255, null=True, blank=True)
    synopsis = models.TextField()
    cast = models.ManyToManyField(People, related_name="films")  # Many-to-many relationship for cast

    def __str__(self):
        return self.title

class Occupations(models.Model):
    occupation_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.occupation_name

class PeopleOccupations(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupations, on_delete=models.CASCADE)

class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name

class PeopleCategories(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Events(models.Model):
    event_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    event_description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return self.event_title

class RelatedPeople(models.Model):
    person = models.ForeignKey(People, related_name='person', on_delete=models.CASCADE)
    related_person = models.ForeignKey(People, related_name='related_person', on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=255)

class Sources(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=255)
    source_url = models.URLField(max_length=500)

    def __str__(self):
        return self.source_name

class Aliases(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255)

    def __str__(self):
        return self.alias_name

class Quotes(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    quote_text = models.TextField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.quote_text[:50]  # Preview of the quote text

class PeopleEvents(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

class SocialMediaLink(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    profile_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.platform}: {self.profile_url}"

class SearchHistory(models.Model):
    search_term = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)
    result_count = models.IntegerField()
    person = models.ForeignKey(People, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.search_date.strftime('%Y-%m-%d %H:%M:%S')} - {self.search_term}"
