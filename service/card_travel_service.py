from db.configure_app import card_travel_initial
from db.db_connection import get_session
from model.card_travel_model import CardTravelModel


session = get_session()
# Se crean los metodos
def get_cards():
 
    return session.query(CardTravelModel).all()

def get_card_by_id(id):
    return session.query(CardTravelModel).filter_by(id=id).first()

