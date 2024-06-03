from datetime import datetime
from django.db.models import QuerySet

from db.models import MovieSession
from services.cinema_hall import get_hall_by_id
from services.movie import get_movie_by_id


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie=get_movie_by_id(movie_id),
        cinema_hall=get_hall_by_id(cinema_hall_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(
        id=movie_session_id
    )


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = get_movie_by_id(movie_id)
    if cinema_hall_id:
        session.cinema_hall = get_hall_by_id(cinema_hall_id)
    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
