from django.contrib import admin
from .models import (
    People, Art, MusicAlbum, Film, Occupations, PeopleOccupations, 
    Categories, PeopleCategories, Events, RelatedPeople, Sources, 
    Aliases, Quotes, PeopleEvents, SocialMediaLink, SearchHistory
)

admin.site.register(People)
admin.site.register(Art)
admin.site.register(MusicAlbum)
admin.site.register(Film)
admin.site.register(Occupations)
admin.site.register(PeopleOccupations)
admin.site.register(Categories)
admin.site.register(PeopleCategories)
admin.site.register(Events)
admin.site.register(RelatedPeople)
admin.site.register(Sources)
admin.site.register(Aliases)
admin.site.register(Quotes)
admin.site.register(PeopleEvents)
admin.site.register(SocialMediaLink)
admin.site.register(SearchHistory)
