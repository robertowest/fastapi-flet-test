from .models import Usuario
from .declarative_base import engine, Base, session


class UsuarioSevices():
    def __init__(self):
        # Base.metadata.create_all(engine)
        pass

    def agregar_usuario(self, username, password, first_name, last_name, email, is_staff):
        busqueda = session.query(Usuario).filter(Usuario.username == username).all()
        if len(busqueda) == 0:
            usuario = Usuario(username=username, password=password, first_name=first_name, last_name=last_name, email=email, is_staff=is_staff)
            session.add(usuario)
            session.commit()
            return True
        else:
            return False

    def editar_usuario(self, username, password, first_name, last_name, email, is_staff, is_active):
        busqueda = session.query(Usuario).filter(Usuario.username == username).all()
        if len(busqueda) == 0:
            usuario = session.query(Usuario).filter(Usuario.username == username).first()
            usuario.username = username
            usuario.password = password
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.is_staff = is_staff
            usuario.is_active = is_active
            session.commit()
            return True
        else:
            return False

    def get_by_id(self, usuario_id):
        return session.query(Usuario).get(usuario_id).__dict__
