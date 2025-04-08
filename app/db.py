from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# URL de la base de datos (PostgreSQL)
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor (engine)
engine = create_engine(DATABASE_URL)

# Crear la clase SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Dependencia para obtener sesión de base de datos en endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
