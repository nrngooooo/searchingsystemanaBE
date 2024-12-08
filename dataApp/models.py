from django.db import models


# Main Person Table
class People(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField()
    profileImage = models.ImageField(upload_to="profile/", blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
    class Meta:
        ordering = ["first_name"]


# Related People (Relationships)
class RelatedPeople(models.Model):
    person = models.ForeignKey(People, related_name="person", on_delete=models.CASCADE)
    related_person = models.ForeignKey(People, related_name="related_person", on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.person.full_name} - {self.relationship_type} - {self.related_person.full_name}"

# Occupations
class Occupations(models.Model):
    occupation_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.occupation_name
    class Meta:
        ordering = ["occupation_name"]

class PeopleOccupations(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupations, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.full_name} - {self.occupation.occupation_name}"

# Categories
class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name
    class Meta:
        ordering = ["category_name"]

class PeopleCategories(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.full_name} - {self.category.category_name}"
# Awards
class Awards(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    date_awarded = models.DateField()
    description = models.TextField(null=True, blank=True)
    person = models.ForeignKey(People, on_delete=models.CASCADE, related_name="awards")

    def __str__(self):
        return f"{self.title} ({self.date_awarded})"
    class Meta:
        ordering = ["title"]

# Education
class Education(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE, related_name="education")
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, null=True, blank=True)
    field_of_study = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"
    class Meta:
        ordering = ["institution_name"]

# Social Media Links
class SocialMediaLink(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    profile_url = models.URLField(max_length=500)
    profile_image = models.ImageField(upload_to="social_media/", blank=True, null=True)

    def __str__(self):
        return f"{self.platform}: {self.username}"

# Genre Table
class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
# Movie Table
class Film(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    release_date = models.DateField()
    synopsis = models.TextField()
    filmImage = models.ImageField(upload_to="film/", blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]


# Movie-Genre Junction Table
class MovieGenre(models.Model):
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.genre.name}"

# Film Roles Table for Acting, Directing, Producing, Writing, etc.
class FilmRole(models.Model):
    ROLE_CHOICES = [
        ("actor", "Actor"),
        ("director", "Director"),
        ("producer", "Producer"),
        ("writer", "Writer"),
    ]

    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="roles")
    person = models.ForeignKey(People, on_delete=models.CASCADE, related_name="film_roles")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    role_name = models.CharField(max_length=255, null=True, blank=True)  # e.g., Character name for actors

    def __str__(self):
        return f"{self.person.full_name} - {self.get_role_display()} in {self.film.title}"


# Music Albums
class MusicAlbum(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    artist = models.ForeignKey(People, on_delete=models.SET_NULL, null=True, blank=True, related_name="music_albums")
    release_date = models.DateField()
    genre = models.CharField(max_length=255, null=True, blank=True)
    albumImage = models.ImageField(upload_to="album/", blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]

# Written Works
class WrittenWorks(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(People, on_delete=models.SET_NULL, null=True, blank=True, related_name="written_works")
    publication_date = models.DateField()
    genre = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    writtenWorksImage = models.ImageField(upload_to="written_works/", blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]

# Artworks
class Art(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    artist = models.ForeignKey(People, on_delete=models.CASCADE, related_name="artworks")
    creation_date = models.DateField()
    artImage = models.ImageField(upload_to="art/", blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]

# Events
class Events(models.Model):
    event_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    event_description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return self.event_title
    class Meta:
        ordering = ["event_title"]

class PeopleEvents(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.person.full_name} - {self.event.event_title}"

# Quotes
class Quotes(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    quote_text = models.TextField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.quote_text[:50]
    class Meta:
        ordering = ["quote_text"]

# Historical Data
class HistoricalEvent(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE, related_name="historical_events")
    event_title = models.CharField(max_length=255)
    event_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.event_title


# Search History
class SearchHistory(models.Model):
    search_term = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)
    result_count = models.IntegerField()
    person = models.ForeignKey(People, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.search_date.strftime('%Y-%m-%d %H:%M:%S')} - {self.search_term}"
