from ninja import NinjaAPI
from chatbot import views

api = NinjaAPI()

api.add_router("/chatbot_api/", )    # You can add a router as an object