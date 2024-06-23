from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:

    sessions = MovieSession.objects.all()

    if session_date:
        sessions = sessions.filter(
            show_time__date=session_date
        )

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> MovieSession:

    movie = get_movie_session_by_id(session_id)

    if show_time:
        movie.show_time = show_time
    if movie_id:
        movie.movie_id = movie_id
    if cinema_hall_id:
        movie.cinema_hall_id = cinema_hall_id
    movie.save()
    return movie


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return get_movie_session_by_id(session_id).delete()
