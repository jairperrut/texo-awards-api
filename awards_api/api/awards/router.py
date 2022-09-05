from fastapi import APIRouter, Depends

from awards_api.db.engine import get_session
from awards_api.api.awards.service import AwardService
from awards_api.api.awards.schema import AwardLoadSchema, AwardDumpSchema, WinnerIntervalSchema

router = APIRouter(prefix="/awards")


@router.get("/", response_model=list[AwardDumpSchema])
def find_all(session=Depends(get_session)):
    service = AwardService(session)
    return service.find()


@router.get("/{award_id}", response_model=AwardDumpSchema)
def find_by_id(award_id, session=Depends(get_session)):
    service = AwardService(session)
    return service.find_by_id(award_id)


@router.post("/", response_model=AwardDumpSchema)
def create(award: AwardLoadSchema, session=Depends(get_session)):
    service = AwardService(session)
    return service.create(award.dict())


@router.put("/{award_id}", response_model=AwardDumpSchema)
def update(award_id, award: AwardLoadSchema, session=Depends(get_session)):
    service = AwardService(session)
    return service.update(award_id, award.dict())


@router.get("/winners/", response_model=WinnerIntervalSchema)
def winners_interval(session=Depends(get_session)):
    service = AwardService(session)
    _min, _max = service.winners_interval()
    return {"min": _min, "max": _max}
