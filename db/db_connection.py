from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


def get_session():
    try:
        db_url = "sqlite:///mydb.db"
        engine = create_engine(db_url, connect_args={"check_same_thread": False})
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return session()
    except Exception as e:
        # En caso de error, imprime un mensaje de error y devuelve None o una indicación de error
        print(f"Error al crear la sesión: {str(e)}")
        raise e

