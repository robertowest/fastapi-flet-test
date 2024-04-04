Esta es una nueva prueba con fastAPI donde estoy intentando ver que estructura de carpeta me gusta más

viejo: estructura por aplicación
nuevo: estructura por contenido

No me decido por una estructura en especial, así que utilizaré el modelo "por aplicación" ya que si es 
proyecto crece demasiado, será más fácil tener todos los componentes agrupados en una única carpeta.

Para obtener el modelo de datos de una base de datos existente, utilizaremos el siguiente comando
```bash
sqlacodegen mysql+mysqlconnector://root:atenea00@localhost/minitwitter
```

Para ejecutar la aplicación:
```bash
uvicorn main:app --port 8080 --reload
```

En el caso de querer utilizar la estructura nueva, la ejecutamos así:
```bash
uvicorn nuevo.api.v1.routes:app --port 8080
```



# estructura de un proyecto nuevo
```text
/proyecto_fastapi
    /app
        __init__.py
        /api
            __init__.py
            /v1
                __init__.py
                /endpoints
                    __init__.py
                    archivo_endpoint.py
                routes.py
            deps.py
        /core
            __init__.py
            config.py
            security.py
        /crud
            __init__.py
            crud_modelo.py
        /db
            __init__.py
            base.py
            session.py
        /models
            __init__.py
            modelo_db.py
        /schemas
            __init__.py
            schema.py
        /services
            __init__.py
            service.py
    /tests
        __init__.py
        test_api.py
    main.py
```

API: Mantén tus endpoints de API separados por versión y/o por funcionalidad dentro de la carpeta /api. Esto hace que sea más fácil versionar tu API y mantenerla organizada.

Modelos (Models): Define los modelos de tu base de datos en /models. Estos modelos representan las tablas en tu base de datos.

Esquemas (Schemas): Usa /schemas para definir esquemas Pydantic que serán utilizados para la validación de datos de entrada y salida de tu API. Estos esquemas actúan como una capa de serialización que separa tus modelos internos de lo que expones a través de tu API.

Operaciones de la Base de Datos (CRUD): Coloca las operaciones de creación, lectura, actualización y eliminación en /crud. Estas funciones interactúan directamente con la base de datos y son invocadas por tus endpoints de API.

Dependencias (Deps): Las dependencias comunes, como la obtención de la sesión de la base de datos o las dependencias de seguridad, pueden ser almacenadas en deps.py.

Núcleo (Core): Configuraciones centrales de la aplicación, como variables de entorno y configuraciones de seguridad, se pueden manejar en /core.

Servicios (Services): La lógica de negocio que podría ser compartida entre diferentes endpoints se puede colocar en /services.

# Uso de Routers y Dependencias

FastAPI facilita la modularización de tus endpoints usando routers. Define routers en tus módulos de API y monta estos routers en tu aplicación principal. Las dependencias, como la conexión a la base de datos y los esquemas de seguridad, pueden ser inyectadas en tus rutas como dependencias.

# Pruebas

Mantén tus pruebas en el directorio /tests. Estructura tus pruebas para que reflejen la estructura de tu aplicación. Usa las herramientas de testing de FastAPI para probar tus endpoints y la lógica de negocio.

# Documentación y Convenciones de Nombres

Además de estructurar bien tu aplicación, sigue las buenas prácticas de codificación y documentación. Documenta tus funciones y clases, y sigue las convenciones de nombres de Python para facilitar la legibilidad y mantenimiento del código.

# Configuración y Despliegue

Considera la configuración para diferentes entornos (desarrollo, pruebas, producción). Utiliza variables de entorno y archivos de configuración para manejar las diferencias entre entornos.

Esta estructura es una guía general y puede ser adaptada según las necesidades específicas de tu proyecto. FastAPI es bastante flexible, permitiéndote estructurar tu aplicación de la manera que mejor se ajuste a tu proyecto.

