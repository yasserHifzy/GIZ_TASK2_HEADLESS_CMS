from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/add")
def addtion(request, a: int, b: int):
    return {"result": a + b}
@api.get("/sub")
def subtraction(request, a: int, b: int):
    return {"result": a - b}