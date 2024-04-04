from pydantic import BaseModel

class PersonaBase(BaseModel):
    nombre: str
    edad: int
    direccion: str

class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(PersonaBase):
    pass

class PersonaInDBBase(PersonaBase):
    id: int

    class Config:
        orm_mode = True

class Persona(PersonaInDBBase):
    pass
