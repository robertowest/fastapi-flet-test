from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from typing import List

from . import services
from . import schemas   # PersonaCreate, Persona, PersonaUpdate
from apps.base import SessionLocal

router = APIRouter()    # APIRouter(prefix='/personas/)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/personas/", response_model=schemas.Persona, tags=['Personas'])
def create_persona_api(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    return services.create_persona(db=db, persona=persona)


@router.get("/personas/", response_model=List[schemas.Persona], tags=['Personas'])
def read_personas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    personas = services.get_personas(db, skip=skip, limit=limit)
    return personas


@router.get("/personas/{persona_id}", response_model=schemas.Persona, tags=['Personas'])
def read_persona(persona_id: int, db: Session = Depends(get_db)):
    db_persona = services.get_persona(db, persona_id=persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@router.put("/personas/{persona_id}", response_model=schemas.Persona, tags=['Personas'])
def update_persona_api(persona_id: int, persona: schemas.PersonaUpdate, db: Session = Depends(get_db)):
    db_persona = services.update_persona(db, persona_id, persona)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@router.delete("/personas/{persona_id}", response_model=schemas.Persona, tags=['Personas'])
def delete_persona_api(persona_id: int, db: Session = Depends(get_db)):
    db_persona = services.delete_persona(db, persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona
