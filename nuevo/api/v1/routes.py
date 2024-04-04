from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from typing import List

from app.crud.crud_persona import *
from app.schemas.schema import PersonaCreate, Persona, PersonaUpdate
from app.db.base import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/personas/", response_model=Persona, tags=['personas'])
def create_persona_api(persona: PersonaCreate, db: Session = Depends(get_db)):
    return create_persona(db=db, persona=persona)


@router.get("/personas/", response_model=List[Persona], tags=['personas'])
def read_personas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    personas = get_personas(db, skip=skip, limit=limit)
    return personas


@router.get("/personas/{persona_id}", response_model=Persona, tags=['personas'])
def read_persona(persona_id: int, db: Session = Depends(get_db)):
    db_persona = get_persona(db, persona_id=persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@router.put("/personas/{persona_id}", response_model=Persona, tags=['personas'])
def update_persona_api(persona_id: int, persona: PersonaUpdate, db: Session = Depends(get_db)):
    db_persona = update_persona(db, persona_id, persona)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@router.delete("/personas/{persona_id}", response_model=Persona, tags=['personas'])
def delete_persona_api(persona_id: int, db: Session = Depends(get_db)):
    db_persona = delete_persona(db, persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


app = FastAPI()
app.include_router(router)
