from pydantic import BaseModel


class StudioBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class StudioDumpSchema(StudioBase):
    id: int
