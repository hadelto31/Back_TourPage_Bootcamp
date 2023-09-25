from fastapi import FastAPI

from db.db_connection import get_session
from model.card_travel_model import CardTravelModel
from model.user_model import UserModel


def initial_setup(app: FastAPI):
    user_initial_db()
    card_travel_initial()


def user_initial_db():
    try:
        session = get_session()  # Obtiene una sesión de la base de datos
        if session:
            initial_data = [
                {"username": "usuario1", "email": "usuario1@example.com"},
                {"username": "usuario2", "email": "usuario2@example.com"},
            ]

            for data in initial_data:
                username = data["username"]
                existing_user = session.query(
                    UserModel).filter_by(username=username).first()
                if not existing_user:
                    new_user = UserModel(**data)
                    session.add(new_user)

            # Confirmar la transacción
            session.commit()
            print("Datos iniciales insertados con éxito.")
    except Exception as e:
        print(f"Error al insertar datos iniciales: {str(e)}")
    finally:
        if session:
            session.close()


def card_travel_initial():
    try:
        session = get_session()  # Obtiene una sesión de la base de datos
        if session:
            initial_data = [
                {
                    "id": 1,
                    "country": "Spain",
                    "city": "Barcelona",
                    "rate": 4.5,
                    "price": 500.0,
                    "image_url": "https://images.pexels.com/photos/1388030/pexels-photo-1388030.jpeg?auto=compress&cs=tinysrgb&w=600"
                },
                {
                    "id": 2,
                    "country": "Italy",
                    "city": "Rome",
                    "rate": 4.8,
                    "price": 600.0,
                    "image_url": "https://images.pexels.com/photos/3892129/pexels-photo-3892129.jpeg?auto=compress&cs=tinysrgb&w=600"
                },
                {
                    "id": 3,
                    "country": "France",
                    "city": "Paris",
                    "rate": 4.9,
                    "price": 700.0,
                    "image_url": "https://images.pexels.com/photos/17152635/pexels-photo-17152635/free-photo-of-francia-punto-de-referencia-paris-flores.jpeg?auto=compress&cs=tinysrgb&w=600"
                },
                {
                    "id": 4,
                    "country": "Japan",
                    "city": "Tokyo",
                    "rate": 4.7,
                    "price": 750.0,
                    "image_url": "https://images.pexels.com/photos/2506923/pexels-photo-2506923.jpeg?auto=compress&cs=tinysrgb&w=600"
                },
                {
                    "id": 5,
                    "country": "USA",
                    "city": "New York",
                    "rate": 4.6,
                    "price": 800.0,
                    "image_url": "https://images.pexels.com/photos/290386/pexels-photo-290386.jpeg?auto=compress&cs=tinysrgb&w=600"
                }
            ]

            for data in initial_data:
                card_id = data["id"]
                existing_card = session.query(
                    CardTravelModel).filter_by(id=card_id).first()
                if not existing_card:
                    new_card = CardTravelModel(**data)
                    print(new_card)
                    session.add(new_card)

            # Confirmar la transacción
            session.commit()
            print("Datos iniciales insertados con éxito.")
    except Exception as e:
        print(f"Error al insertar datos iniciales: {str(e)}")
    finally:
        if session:
            session.close()
