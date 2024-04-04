import pyodbc

from contextlib import contextmanager

from config import settings


"""
Uso:
    ms_db = MSSQL()
    with ms_db.cursor() as cursor:
            cursor.execute("SELECT @@version;")
            print(cursor.fetchall())
"""
class MSSQL():
    """ 
    Colección de métodos para base de datos MS SQL Server
    """

    def __init__(self):
        self.driver = settings.DB_DRIVER
        self.user = settings.DB_USER
        self.pwd = settings.DB_PASS
        self.host = settings.DB_HOST
        self.port = settings.DB_PORT
        self.db = settings.DB_NAME
        self._connection = None
        # servidor
        # self.connection_string = f"Driver={self.driver};Server={self.host};Port={self.port};Database={self.db};Trusted_Connection=yes;"
        self.connection_string = f"DRIVER={self.driver};SERVER={self.host};PORT={self.port};DATABASE={self.db};UID={self.user};PWD={self.pwd};"
        self.connect()
        pyodbc.pooling = False

    def __repr__(self):
        return f"MS-SQLServer('{self.user}', '{self.host}', '{self.port}', '{self.db}')"

    def __str__(self):
        return f"MS-SQLServer módulo para STP en {self.host}"

    def __del__(self):
        self.close()

    def connect(self, connection_string = None):
        try:
            if connection_string == None:
                connection_string = self.connection_string
            self._connection = pyodbc.connect(self.connection_string)
            print('Conexión :', self.connection_string)
        except Exception:
            print("ERROR: No es posible conectarse a la base de datos.")
            exit(-1)

    def close(self):
        try:
            self._connection.close()
            self._connection = None
        except pyodbc.Error as e:
            print(e)

    @contextmanager
    def cursor(self, commit: bool = False):
        """
        El contextmanager de usará un cursor para operaciones de bases de datos.
        Esta función debe usarse para cualquier consulta u operación de la base de datos que sea necesario.

        :parámetro
        commit: booleano que define si se harán cambios en la base de datos
        """
        if self._connection == None:
            self.connect()  # abre conexión
        cursor = self._connection.cursor()
        try:
            yield cursor
        except pyodbc.DatabaseError as err:
            print("DatabaseError {} ".format(err))
            cursor.rollback()
            raise err
        else:
            if commit:
                cursor.commit()
        finally:
            cursor.close()

    def result_to_dict(cursor):
        """
        Función para devolver los resultados de SQL como un dict.
        Mapea los nombres y valores de la columna para el dict 
        Devuelve 'no se encontraron resultados' si no hay registros
        """
        try: 
            result = []
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result.append(dict(zip(columns,row)))

            # comprueba si hay registros
            if len(result) > 0:
                ret = result
            else:
                ret = {"status": "OK", "message": "No se encontraron registros"}

        except pyodbc.Error as e:
            print(e)
            ret = {"status": "Error", "message": "Error interno al consultar la base de datos"}
        
        return ret


# if __name__ == '__main__':
#     from ..core.config import settings

#     ms_db = MSSQL()
#     with ms_db.cursor() as cursor:
#             cursor.execute("SELECT @@version;")
#             print(cursor.fetchall())
