from django.shortcuts import render
from ninja import Router, Schema
from .Chatbot_Logic import ChatBot

class ResponseSchema(Schema):
    message: str

router = Router()
chatbot = ChatBot()

@router.post('/message', response=ResponseSchema)
def get_message(request, characters: str = '', message: str = ''):
    chatbot.set_pramater(characters, message)
    response = chatbot.response()
    return response