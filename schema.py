import traceback
from django.db import transaction
from django.db.models import Q
import graphene
from graphene_django import DjangoObjectType
from dataApp.models import *
import logging

logger = logging.getLogger("main")

# Define GraphQL Object Types for each model
class PeopleType(DjangoObjectType):
    class Meta:
        model = People

class ArtType(DjangoObjectType):
    class Meta:
        model = Art

class MusicAlbumType(DjangoObjectType):
    class Meta:
        model = MusicAlbum

class FilmType(DjangoObjectType):
    class Meta:
        model = Film

class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupations

class CategoryType(DjangoObjectType):
    class Meta:
        model = Categories

class EventType(DjangoObjectType):
    class Meta:
        model = Events

class RelatedPeopleType(DjangoObjectType):
    class Meta:
        model = RelatedPeople

class PeopleOccupationsType(DjangoObjectType):
    class Meta:
        model = PeopleOccupations

class PeopleCategoriesType(DjangoObjectType):
    class Meta:
        model = PeopleCategories

class EducationType(DjangoObjectType):
    class Meta:
        model = Education

class AwardsType(DjangoObjectType):
    class Meta:
        model = Awards

class PeopleEventsType(DjangoObjectType):
    class Meta:
        model = PeopleEvents

class WrittenWorksType(DjangoObjectType):
    class Meta:
        model = WrittenWorks

class HistoricalEventType(DjangoObjectType):
    class Meta:
        model = HistoricalEvent

class QuotesType(DjangoObjectType):
    class Meta:
        model = Quotes

class SocialMediaLinkType(DjangoObjectType):
    class Meta:
        model = SocialMediaLink

class SearchHistoryType(DjangoObjectType):
    class Meta:
        model = SearchHistory

class FilmRoleType(DjangoObjectType):
    class Meta:
        model = FilmRole
class MovieGenreType(DjangoObjectType):
    class Meta:
        model = MovieGenre
class GenreType(DjangoObjectType):
    class Meta:
        model = Genre

# Queries for each model
class Query(graphene.ObjectType):
    # lists
    art_list = graphene.List(ArtType)
    music_album_list = graphene.List(MusicAlbumType)
    film_list = graphene.List(FilmType)
    filmrole_list = graphene.List(FilmRoleType)
    relatedperson_list = graphene.List(RelatedPeopleType)
    moviegenre_list = graphene.List(MovieGenreType)
    genre_list = graphene.List(GenreType)
    quotes_list = graphene.List(QuotesType)
    search_history_list = graphene.List(SearchHistoryType)
    socialmedialink_list = graphene.List(SocialMediaLinkType)
    occupation_list = graphene.List(OccupationType)
    category_list = graphene.List(CategoryType)
    event_list = graphene.List(EventType)
    people_list = graphene.List(PeopleType)
    people_occupations_list = graphene.List(PeopleOccupationsType)
    people_categories_list = graphene.List(PeopleCategoriesType)
    people_events_list = graphene.List(PeopleEventsType)
    education_list = graphene.List(EducationType)
    awards_list = graphene.List(AwardsType)
    written_works_list = graphene.List(WrittenWorksType)
    historical_events_list = graphene.List(HistoricalEventType)

    person = graphene.Field(PeopleType, id=graphene.Int())
    search_people = graphene.List(PeopleType, search_term=graphene.String())

    def resolve_people_occupations_list(self, info):
        return PeopleOccupations.objects.all()

    def resolve_people_categories_list(self, info):
        return PeopleCategories.objects.all()

    def resolve_education_list(self, info):
        return Education.objects.all()

    def resolve_awards_list(self, info):
        return Awards.objects.all()

    def resolve_people_events_list(self, info):
        return PeopleEvents.objects.all()

    def resolve_written_works_list(self, info):
        return WrittenWorks.objects.all()

    def resolve_historical_events_list(self, info):
        return HistoricalEvent.objects.all()
    def resolve_people_list(self, info):
        return People.objects.all().order_by("first_name", "last_name")

    def resolve_person(self, info, id):
        return People.objects.get(pk=id)

    def resolve_search_people(self, info, search_term):
        return People.objects.filter(
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(nickname__icontains=search_term) |
            Q(biography__icontains=search_term)
        )

    def resolve_art_list(self, info):
        return Art.objects.all().order_by("title")

    def resolve_music_album_list(self, info):
        return MusicAlbum.objects.all().order_by("title")

    def resolve_film_list(self, info):
        return Film.objects.all().order_by("title")

    def resolve_occupation_list(self, info):
        return Occupations.objects.all().order_by("occupation_name")

    def resolve_category_list(self, info):
        return Categories.objects.all().order_by("category_name")

    def resolve_event_list(self, info):
        return Events.objects.all().order_by("event_title")


# Input Types for each model
class PeopleInput(graphene.InputObjectType):
    first_name = graphene.String(description='Нэр', required=True)
    last_name = graphene.String(description='Овог', required=True)
    date_of_birth = graphene.Date(description='Төрсөн огноо')
    place_of_birth = graphene.String(description='Төрсөн газар', required=True)
    date_of_death = graphene.Date(description='Нас барсан огноо')
    biography = graphene.String(description='Намтар')
    profile_image = graphene.String(description='Профайл зураг')

class ArtInput(graphene.InputObjectType):
    title = graphene.String(description='Уран бүтээл', required=True)
    artist_id = graphene.ID(description='Уран бүтээлчийн ID', required=True)
    creation_date = graphene.Date(description='Бүтээл төрсөн өдөр')
    description = graphene.String(description='Тайлбар')

class MusicAlbumInput(graphene.InputObjectType):
    title = graphene.String(description='Цомгийн нэр', required=True)
    artist_id = graphene.ID(description='Цомгийн уран бүтээлчийн ID', required=True)
    release_date = graphene.Date(description='Дуу цацагдсан огноо')
    genre = graphene.String(description='Жанр')

class FilmInput(graphene.InputObjectType):
    title = graphene.String(description='Кино нэр', required=True)
    director_id = graphene.ID(description='Найруулагч', required=True)
    release_date = graphene.Date(description='Нээлтээ хийсэн огноо')
    genre = graphene.String(description='Жанр')
    synopsis = graphene.String(description='Товч тойм')

class OccupationInput(graphene.InputObjectType):
    occupation_name = graphene.String(description='Мэргэжлийн нэр', required=True)

class CategoryInput(graphene.InputObjectType):
    category_name = graphene.String(description='Бүлгийн нэр', required=True)

class EventInput(graphene.InputObjectType):
    event_title = graphene.String(description='Үйл явдал', required=True)
    event_date = graphene.Date(description='Үйл явдлын огноо')
    event_description = graphene.String(description='Үйл явдлын тайлбар')

class SocialMediaLinkInput(graphene.InputObjectType):
    platform = graphene.String(description='Сошиал медиа')
    profile_url = graphene.String(description='Профайлын холбоос')

#*********************************** Mutations ***********************************

class CreatePerson(graphene.Mutation):
    class Arguments:
        data = PeopleInput(required=True)
    
    person = graphene.Field(PeopleType)

    def mutate(self, info, data):   
        person = People.objects.create(**data)
        return CreatePerson(person=person)

class UpdatePerson(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PeopleInput(required=True)

    person = graphene.Field(PeopleType)

    def mutate(self, info, id, input):
        person = People.objects.get(pk=id)
        for key, value in input.items():
            setattr(person, key, value)
        person.save()
        return UpdatePerson(person=person)

class DeletePerson(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        person = People.objects.get(pk=id)
        person.delete()
        return DeletePerson(success=True)

class CreateArt(graphene.Mutation):
    class Arguments:
        data = ArtInput(required=True)

    artwork = graphene.Field(ArtType)

    def mutate(self, info, data):
        artwork = Art.objects.create(**data)
        return CreateArt(artwork=artwork)

class CreateMusicAlbum(graphene.Mutation):
    class Arguments:
        data = MusicAlbumInput(required=True)

    album = graphene.Field(MusicAlbumType)

    def mutate(self, info, data):
        album = MusicAlbum.objects.create(**data)
        return CreateMusicAlbum(album=album)

class CreateFilm(graphene.Mutation):
    class Arguments:
        data = FilmInput(required=True)

    film = graphene.Field(FilmType)

    def mutate(self, info, data):
        film = Film.objects.create(**data)
        return CreateFilm(film=film)

class CreateOccupation(graphene.Mutation):
    class Arguments:
        data = OccupationInput(required=True)

    occupation = graphene.Field(OccupationType)

    def mutate(self, info, data):
        occupation = Occupations.objects.create(**data)
        return CreateOccupation(occupation=occupation)

class CreateCategory(graphene.Mutation):
    class Arguments:
        data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, data):
        category = Categories.objects.create(**data)
        return CreateCategory(category=category)

class CreateEvent(graphene.Mutation):
    class Arguments:
        data = EventInput(required=True)

    event = graphene.Field(EventType)

    def mutate(self, info, data):
        event = Events.objects.create(**data)
        return CreateEvent(event=event)

class CreateSocialMediaLink(graphene.Mutation):
    class Arguments:
        data = SocialMediaLinkInput(required=True)

    link = graphene.Field(SocialMediaLinkType)

    def mutate(self, info, data):
        link = SocialMediaLink.objects.create(**data)
        return CreateSocialMediaLink(link=link)

# Create similar mutations for other models: Art, MusicAlbum, Film, etc.

#***************** 🔥🔥🔥 Wiring up the mutations 🔥🔥🔥 *******************
class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()
    # Register other mutations similarly for other models

#***************** 🔥🔥🔥 Defining schema object for graphql view 🔥🔥🔥 *******************
# With rollback
class AtomicSchema(graphene.Schema):
    def execute(self, *args, **kwargs):
        with transaction.atomic():
            result = super().execute(*args, **kwargs)
            if result.errors:
                transaction.set_rollback(True)
                logger.error(
                    f"GQL Error Traceback: {result.errors}",
                    extra={"details": traceback.format_exc()},
                )
            return result

schema = AtomicSchema(query=Query, mutation=Mutation)
