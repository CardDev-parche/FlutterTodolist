from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)





data = [
    {
        "title":"MOBA",
        "subtitle":"เกมแนว MOBA หรือเรียกชื่อเต็มว่า (Multiplayer Online Battle Arena)",
        "image_url":"https://raw.githubusercontent.com/CardDev-parche/BasicAPI/main/Image%20Uploads/photo-1624138149925-6c1dd2d60460.jpg",
        "detail":"MOBA คือ เกมต่อสู้กันระหว่างสองฝ่ายและจะต้องเลือกตัวละครในการเล่น และในแต่ละตัวละครก็จะมีความสามารถไม่เหมือนกันเรียกว่าสกิล จำเป็นที่จะต้องใช้ทักษะในการเล่นและการเลือกซื้อไอเทมต่างๆ จากร้านค้าเพื่อเสริมความสามารถให้กับตัวละครนั้นๆเพื่อช่วยในการทำลายฐานอีกฝ่าย หรือสนับสนุนเพื่อนในทีม เมื่อใดที่เราทำลายฐานฝ่ายตรงข้ามจนหมดเราก็ชนะ โดยเกมนี้มักจะเป็นระบบออนไลน์ และใช้ความสามัคคีบวกการวางแผนพอสมควร"
    },
    {
        "title":"FPS",
        "subtitle":"เกมแนว FPS หรือเรียกชื่อเต็มว่า (First Person Shooter)",
        "image_url":"https://raw.githubusercontent.com/CardDev-parche/BasicAPI/main/Image%20Uploads/photo-1542751371-adc38448a05e.jpg",
        "detail":"FPS หรือที่เรียกกันว่า เกมยิงมุมมองบุคคลที่หนึ่ง หรือเรียกง่ายๆว่าเป็นวิดีโอเกมประเภทที่จุดศูนย์กลางอยู่ที่อาวุธปืน  โดยใช้อาวุธโจมตีมองผ่านจากดวงตาของตัวละครเอกในเกม  คล้ายมุมมองของภาพถ่ายซึ่งเกือบจะทั้งหมดองค์ประกอบหลักของเกมแนวนี้  คือการโจมตีโดยจะใช้อาวุธปืนเบารอบตัวที่สามารถพกพาไปได้เป็นหลัก  และเกมประเภทนี้ได้รับความนิยมอย่างมาก  เพราะจะให้ความรู้สึกเหมือนคุณเป็นตัวละครนั้นได้สวมบทบาทในเกมเล่นไปตามเกมหรือเนื้อเรื่องของเกม"
    },
    {
        "title":"MMORPG",
        "subtitle":"เกมแนว MMORPG หรือเรียกชื่อเต็มว่า (Massive Multiplayer Online Role-Playing Game)",
        "image_url":"https://raw.githubusercontent.com/CardDev-parche/BasicAPI/main/Image%20Uploads/0975551001576667926549_FF14NowHas18MPlayers_2.jpg",
        "detail":"MMORPG ย่อมาจากเกมเล่นตามบทบาทออนไลน์ที่มีผู้เล่นหลายคนซึ่งเป็นเกมออนไลน์ที่มีผู้เล่นจำนวนมาก เป็นเกมสวมบทบาททางคอมพิวเตอร์ ที่เกิดขึ้นในโลกเสมือนจริงออนไลน์ที่มีผู้เล่นหลายคนเข้ามาเล่นในเวลาเดียวกันนับร้อยหรือพันคน โดยผ่านระบบเครือข่ายคอมพิวเตอร์ขนาดใหญ่ และผู้เล่นแต่ละคนจะสวมบทบาทเป็นตัวละครตัวหนึ่งในโลกนั้นด้วย"
    }
]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})