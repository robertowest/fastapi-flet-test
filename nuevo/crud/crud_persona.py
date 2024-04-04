from sqlalchemy.orm import Session
from ..models.modelo_db import Persona
from ..schemas.schema import PersonaCreate, PersonaUpdate


def get_persona(db: Session, persona_id: int):
    return db.query(Persona).filter(Persona.id == persona_id).first()


def get_personas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Persona).offset(skip).limit(limit).all()


def create_persona(db: Session, persona: PersonaCreate):
    db_persona = Persona(nombre=persona.nombre, edad=persona.edad, direccion=persona.direccion)
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona


def update_persona(db: Session, persona_id: int, persona: PersonaUpdate):
    db_persona = get_persona(db, persona_id)
    if db_persona:
        db_persona.nombre = persona.nombre
        db_persona.edad = persona.edad
        db_persona.direccion = persona.direccion
        db.commit()
        db.refresh(db_persona)
    return db_persona


def delete_persona(db: Session, persona_id: int):
    db_persona = get_persona(db, persona_id)
    if db_persona:
        db.delete(db_persona)
        db.commit()
    return db_persona
