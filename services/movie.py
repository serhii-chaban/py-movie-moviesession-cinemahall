from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )

    if genres_ids and not actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids and not genres_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


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
        movie_inst.actors.set(actors_ids)
    if genres_ids:
        movie_inst.genres.set(genres_ids)
