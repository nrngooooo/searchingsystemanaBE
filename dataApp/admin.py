from django.contrib import admin
from .models import *

class PeopleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    search_fields = ("first_name", "last_name", "nickname")

class OccupationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("occupation_name",)}

class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "release_date")
    list_filter = ("release_date",)

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}

class ArtAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class MusicAlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class WrittenWorksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("event_title",)}

# Register all models with appropriate admin classes
admin.site.register(People, PeopleAdmin)
admin.site.register(RelatedPeople)
admin.site.register(Occupations, OccupationsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Awards)
admin.site.register(Education)
admin.site.register(SocialMediaLink)
admin.site.register(Art, ArtAdmin)
admin.site.register(MusicAlbum, MusicAlbumAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(FilmRole)
admin.site.register(MovieGenre)
admin.site.register(Genre, GenreAdmin)
admin.site.register(WrittenWorks, WrittenWorksAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(PeopleCategories)
admin.site.register(PeopleOccupations)
admin.site.register(PeopleEvents)
admin.site.register(Quotes)
admin.site.register(HistoricalEvent)
admin.site.register(SearchHistory)
