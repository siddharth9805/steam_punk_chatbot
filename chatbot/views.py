from django.shortcuts import render
from ninja import Router, Schema
from .Chatbot_Logic import ChatBot

class ResponseSchema(Schema):
    message: str
    

router = Router()
chatbot = ChatBot()

@router.post('/message')
def get_message(request, characters: str = '', message: str = ''):
    chatbot.set_pramater(characters, message)
    return {"message": "Success"}

@router.post('/generate_message', response=ResponseSchema)
def generate_message(request):
    response = chatbot.response()
    return response