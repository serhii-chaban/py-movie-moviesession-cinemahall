from django.db.models import QuerySet
from db.models import Actor, Genre, Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:

    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.all().filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )

    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie_inst = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if actors_ids:
        for actor in actors_ids:
            movie_inst.actors.add(Actor.objects.get(id=actor))
    if genres_ids:
        for genre in genres_ids:
            movie_inst.genres.add(Genre.objects.get(id=genre))
