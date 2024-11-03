from django.shortcuts import render
from ninja import Router

router = Router()

@router.get('/message')
async def get_message(request, characters: str = '', message: str = ''):
    pass