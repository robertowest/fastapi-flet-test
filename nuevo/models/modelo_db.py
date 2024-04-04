from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    edad = Column(Integer)
    direccion = Column(String)

    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __repr__(self):
        return f'Persona({self.nombre}, {self.edad}, {self.direccion})'

    def __str__(self):
        return self.nombre
