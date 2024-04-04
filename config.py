"""
Archivo de configuración general
"""
import os

from dotenv import load_dotenv


class Settings:
    PROJECT_NAME:str = "Remesa SAP"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Desarrollo de las API's necesarias para la nueva app desarrollada en <b>Flet</b>"

    load_dotenv()   # cargamos variables de entorno

    # DataBase
    DB_DRIVER: str = os.getenv('DB_DRIVER')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: int = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASS: str = os.getenv('DB_PASS')


settings = Settings()
