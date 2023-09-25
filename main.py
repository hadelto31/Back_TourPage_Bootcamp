from fastapi import FastAPI
from db.configure_app import initial_setup
from db.db_connection import get_session
from model.card_travel_model import CardTravelModel
from model.user_model import UserModel
from service.card_travel_service import get_card_by_id, get_cards
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

initial_setup(app)

# Configura middleware CORS para permitir solicitudes desde el dominio de tu aplicación 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.18.15:8081"],  # dirección IP y puerto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    session = get_session()
    
    return session.query(UserModel).all()

@app.get("/card_travel")
async def root():    
    
    return get_cards()


@app.get("/card_travel/{id}")
async def card_by_id(id: int):
    return get_card_by_id(id)
    
    


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
