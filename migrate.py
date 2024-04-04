import app.db.base as db
from app.models.modelo_db import Persona


def run():
    session = db.SessionLocal()
    p1 = Persona('Ainara', 20, 'mi casa')
    session.add(p1)
    p2 = Persona('Gael', 15, 'mi casa')
    session.add(p2)
    session.commit()
    print(p1.id)
    print(p2.id)


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()


# ejecutamos: python migrate.py para crear las tablas del modelo seleccionado
# uvicorn app.api.v1.routes:app --port 8080