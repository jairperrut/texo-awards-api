
import csv
import logging
from sqlalchemy import func

from awards_api.service import CRUDService
from awards_api.api.awards.models import Award
from awards_api.api.studios.models import Studio
from awards_api.api.producers.models import Producer
from awards_api.api.movies.models import Movie

logger = logging.getLogger(__name__)


class AwardService(CRUDService):

    def __init__(self, session):
        super().__init__(session, Award)

    def load_from_csv(self, file_path: str):
        service_producer = CRUDService(self.repository.session, Producer)
        service_studio = CRUDService(self.repository.session, Studio)
        service_movie = CRUDService(self.repository.session, Movie)

        with open(file_path) as file:
            print("Loading movies CSV...")
            data = csv.DictReader(file, delimiter=';')
            for row in data:
                award = self.repository.find({'year': row['year']}).join(Movie).filter(Movie.title == row['title']).first()
                if not award:
                    producer = service_producer.get_or_create({"name": row['producers']})
                    studio = service_studio.get_or_create({"name": row['studios']})
                    movie = service_movie.get_or_create({'title': row['title'], 'producer_id': producer.id, 'studio_id': studio.id})
                    winner = row['winner'] == 'yes'
                    print(f'Adding award: {row["year"]} | {row["title"]}')
                    self.create({'year': row['year'], 'movie_id': movie.id, 'winner': winner})

    def winners_interval(self):
        window_func = func.lag(Award.year).over(partition_by=Producer.id, order_by=Award.year)
        cte = self.repository.session.query(
            Award,
            Award.year.label("followingWin"),
            Producer.name.label("producer"),
            window_func.label('previousWin'),
            (Award.year - window_func).label('interval')
        ).join(Award.movie, Movie.producer).filter(Award.winner.is_(True)).cte()
        min_interval = self.repository.session.query(cte).filter(cte.c.interval == self.repository.session.query(func.min(cte.c.interval)).scalar_subquery()).all()
        max_interval = self.repository.session.query(cte).filter(cte.c.interval == self.repository.session.query(func.max(cte.c.interval)).scalar_subquery()).all()
        return min_interval, max_interval
