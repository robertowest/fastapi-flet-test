# from sqlalchemy import Table, Column
# from sqlalchemy.sql.sqltypes import Integer, String

# from db.mysql import meta, engine


# usuarios = Table(
#     'usuarios', meta, 
#     Column('id', Integer, primary_key=True), 
#     Column('username', String(30)), 
#     Column('password', String(128)),
#     Column('first_name', String(30)),
#     Column('last_name', String(30)),
#     Column('email', String(75)),
# )

# meta.create_all(engine) # estableciendo conexion con la db para la creacion de la table





# # CREATE TABLE `auth_user` (
# #   `id` int NOT NULL AUTO_INCREMENT,
# #   `username` varchar(30) NOT NULL,
# #   `password` varchar(128) NOT NULL,
# #   `first_name` varchar(30) NOT NULL,
# #   `last_name` varchar(30) NOT NULL,
# #   `email` varchar(75) NOT NULL,
# #   `is_superuser` tinyint(1) NOT NULL,
# #   `is_staff` tinyint(1) NOT NULL,
# #   `is_active` tinyint(1) NOT NULL,
# #   `date_joined` datetime(6) NOT NULL,
# #   `last_login` datetime(6) NOT NULL,

# #   PRIMARY KEY (`id`),
# #   UNIQUE KEY `username` (`username`)
# # ) ENGI


import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Usuario(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    is_staff = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    # medio = Column(Enum(Medio))
    # canciones = relationship('Cancion', secondary='album_cancion')        # Foreng
