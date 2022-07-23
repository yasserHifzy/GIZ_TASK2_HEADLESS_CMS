from django.shortcuts import render
from ninja import Router



tools_cotrler= Router()
@tools_cotrler.get('/')
def add(request,a:int,b:int):
    return{'result': a + b}

@tools_cotrler.get('/sub/ a-b')
def sub(request,a:int,b:int):
    return{'result': a - b}

#@tools_cotrler.post("/create")
#def add_users(repuest,paylod:Ente):
    return paylod.dict()