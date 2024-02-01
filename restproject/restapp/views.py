from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .CommentSerialaizer import CommentSerialaizerIn, CommentSerialaizerOut, ItemSerialaizer
from .models import Comment


@api_view(["GET"])
def FirstGet(request):
    if request.method == "GET":
        return Response({"message": "My first get request"})
@api_view(["POST"])
def FirstPost(request):
    if request.method == "POST":
        # alowedLevel = ["B3","B4"]
        comment = Comment(**CommentSerialaizerIn(data=JSONParser().parse(io.BytesIO(request.body))).data)

        return Response(comment.status)
        # data = request.data
        # print(data)
        # return Response({"message": "My first post request"})


# @api_view(["POST"])
# def HumanPost(request):
#     if request.method == "POST":
        # data = request.data
        # if int(data['age']) > 25 and data["Level"] > str("B3"):
        #     print(data["name"])
        #     return Response({"message": f"{data['name']} Good Human"})
        # else:
        #     return Response({"message": f"{data['name']} Bad Human"})

@api_view(["GET"])
def SecondPost(request):
    comment = Comment.objects.get()
    serialaize = CommentSerialaizerOut(comment)
    json = JSONRenderer().render(serialaize.data)
    return Response(json)

@api_view(["POST"])
def ItemPost(request):
    if request.method == "POST":

        item = Item(**ItemSerialaizer(data=JSONParser().parse(io.BytesIO(request.body))).data)

        return Response(Item)
