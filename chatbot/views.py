from django.shortcuts import render
from ninja import Router, Schema
from .Chatbot_Logic import ChatBot

class ResponseSchema(Schema):
    message: str

class MessageSchema(Schema):
    characters: str
    message: str

router = Router()
chatbot = ChatBot()

@router.post('/message', response=ResponseSchema)
def get_message(request, data: MessageSchema):
    chatbot.set_pramater(data.characters, data.message)
    response = chatbot.response()
    print(response)
    return response