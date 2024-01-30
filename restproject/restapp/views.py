from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def FirstGet(request):
    if request.method == "GET":
        return Response({"message": "My first get request"})
@api_view(["POST"])
def FirstPost(request):
    if request.method == "POST":
        data = request.data
        print(data)
        return Response({"message": "My first post request"})

@api_view(["POST"])
def HumanPost(request):
    if request.method == "POST":
        data = request.data
        if int(data['age']) > 25 and data["Level"] > str("B3"):
            print(data["name"])
            return Response({"message": f"{data['name']} Good Human"})
        else:
            return Response({"message": f"{data['name']} Bad Human"})

