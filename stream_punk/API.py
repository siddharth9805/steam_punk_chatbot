from ninja import NinjaAPI
from chatbot import views

api = NinjaAPI()

api.add_router("/chatbot_api/", views.router)    # You can add a router as an object