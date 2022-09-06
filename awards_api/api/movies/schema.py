from pydantic import BaseModel

from awards_api.api.studios.schema import StudioDumpSchema
from awards_api.api.producers.schema import ProducerDumpSchema


class MovieBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class MovieDumpSchema(MovieBase):
    id: int
    studios: list[StudioDumpSchema]
    producers: list[ProducerDumpSchema]
