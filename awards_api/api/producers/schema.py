from pydantic import BaseModel


class ProducerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ProducerDumpSchema(ProducerBase):
    id: int
