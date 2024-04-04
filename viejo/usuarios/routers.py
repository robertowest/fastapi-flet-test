from fastapi import APIRouter, Response, status

# from db.mysql import conn
from .models import Usuario
# from .schemas import Usuario
# from starlette.status import HTTP_204_NO_CONTENT


urlRouter = APIRouter()


# @urlRouter.get('/usuarios', response_model=list[Usuario], tags=['usuarios'])
# def get_usuarios():
#     return conn.execute(usuarios.select()).fetchall()  # consulta sql


# @urlRouter.post('/usuario/nuevo', response_model=Usuario, tags=['usuarios'])
# def create_usuario(usuario: Usuario):
#     new_usuario = {'username': usuario.username, 'email': usuario.email,
#                    'first_name': usuario.first_name, 'last_name': usuario.last_name}
#     result = conn.execute(usuarios.insert().values(new_usuario))
#     print(result.lastrowid)
#     return conn.execute(usuarios.select().where(usuarios.c.id == result.lastrowid)).first()


# @urlRouter.get('/usuario/{id}', response_model=Usuario, tags=['usuarios'])
# def get_usuario(id: str):
#     return conn.execute(usuarios.select().where(usuarios.c.id == id)).first()


# @urlRouter.delete('/usuario/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['usuarios'])
# def delete_usuario(id: str):
#     result = conn.execute(usuarios.delete().where(usuarios.c.id == id))
#     return Response(status_code=HTTP_204_NO_CONTENT)


# @urlRouter.put('/usuario/{id}', response_model=Usuario, tags=['usuarios'])
# def update_usuario(id: str, usuario: Usuario):
#     conn.execute(usuarios.update().values(name=usuario.name, 
#     email=usuario.email, first_name=usuario.first_name, last_name=usuario.last_name).where(usuarios.c.id == id))
#     return conn.execute(usuarios.select().where(usuarios.c.id == id)).first()

from .services import UsuarioSevices

@urlRouter.get('/usuarios', response_model=list[Usuario], tags=['usuarios'])
def get_usuarios():
    return UsuarioSevices.get_by_id(1)
