from pydantic import BaseModel

from awards_api.api.movies.schema import MovieDumpSchema


class AwardBase(BaseModel):
    year: int
    winner: bool

    class Config:
        orm_mode = True


class AwardLoadSchema(AwardBase):
    year: int
    movie_id: int
    winner: bool


class AwardDumpSchema(AwardBase):
    id: int
    movie: MovieDumpSchema

    class Config:
        orm_mode = True


class WinnerSchema(BaseModel):
    producer: str
    interval: int
    previousWin: int
    followingWin: int

    class Config:
        orm_mode = True


class WinnerIntervalSchema(BaseModel):
    min: list[WinnerSchema]
    max: list[WinnerSchema]
