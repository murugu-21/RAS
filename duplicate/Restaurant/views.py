import hashlib 
from .serializers import *
from .models import *
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.core.mail import send_mail
from threading import Thread
import traceback
import random
import csv
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from django.db import connection
from django.http import HttpResponse
def mysql_api(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
    return row

@api_view(['POST'])
def login_check(request):
    try:
        if(request.method == 'POST'):
            current_email = request.data.get("email")
            current_password = request.data.get('password')
            
            try:
                login_row = Login.objects.get(pk=current_email)
            except:
                return Response("Email not valid")
            
            if(login_row.password == hashlib.sha256(current_password.encode()).hexdigest()):
                return Response({"email":current_email, "type":login_row.type})    
            else:
                return Response('Email or password is wrong')
    except:
        traceback.print_exc()

@api_view(['POST'])
def get_users(request):
    if(request.method == 'POST'):
        try:
            users = list(Login.objects.all().values())
            return Response(users)
        except:
            return Response([])
            
@api_view(['POST'])
def delete_user(request):
    if(request.method == 'POST'):
        current_email = request.data['email']
        try:
            login_row = Login.objects.get(pk=current_email)
            login_row.delete()
            users = list(Login.objects.all().values())
            return Response(users)
            
        except:
            traceback.print_exc()
            return Response("Try again later")
    
@api_view(['POST'])
def create_user(request):
    if(request.method == 'POST'):
        
        try:
            data = request.data
            
            if Login.objects.filter(pk=data["email"]).exists():
                return Response(data["email"] + ' already exists')
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
      
            pat = re.compile(reg)                 
            mat = re.search(pat, data["password"])
            if mat:
                new_user = Login(email= data["email"], password= hashlib.sha256(data["password"].encode()).hexdigest(), type= data["type"])
                new_user.save()
                return Response('success')
            else:
                return Response("Password should contain 1 lowercase, 1 uppercase, 1 special character, and 8 - 20 characters")
        except:
            return Response('db error')
        
def gen_mail(email):
    try:
        user = Login.objects.get(pk=email)
        otp = ''.join([str(random.randint(0,9)) for _ in range(7)])
        send_mail(
        'Otp for ras',
        'your otp for changing password is ' + otp,
        'hari.19cs@kct.ac.in',
        [user.email],                    
        fail_silently=False,
        )
        user.otp = otp
        user.save()
    except:
        traceback.print_exc()

@api_view(["POST"])
def forgot_password(request):
    if(request.method == 'POST'):
        data = request.data
        
        try:
            if Login.objects.filter(pk=data["email"]).exists():
                t = Thread(target=gen_mail, args=(data["email"], ))
                t.start()
                return (Response({"cango": True}))
            else:
                return Response(data["email"] + " does not exists")
        except:
            traceback.print_exc()
            return Response("Try After Some Time")

@api_view(['POST'])
def otp_validation(request):
    if(request.method == 'POST'):
        try:
            data = request.data
            if data["number"] == Login.objects.get(pk=data["email"]).otp:
                return (Response({"cango": True}))
                
            else:
                return Response("Otp Invalid")
        except:
            traceback.print_exc()

@api_view(['POST'])
def change_password(request):
    if(request.method == 'POST'):
        data = request.data
        user = Login.objects.get(pk=data["email"])
        if (data["otp"] == user.otp): 
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
      
            pat = re.compile(reg)                 
            mat = re.search(pat, data["password"])
            if mat: 
                user.password = hashlib.sha256(data["password"].encode()).hexdigest()
                user.otp = ""
                user.save()
                return (Response({"cango": True}))

            else:
                return Response("Passwors should match given constraints")
            
        else:
            return Response("Otp Invalid")

@api_view(['POST'])
def get_foods(request):
    query = "select item_code, name, price from food where food.isvisible = 1"
    result = mysql_api(query)
    return Response(result)

@api_view(['POST'])
def update_price(request):
    try:
        changed = request.data
        for item in changed:
            query = "update food set price={} where item_code={}".format(changed[item], item)
            result = mysql_api(query)
            print(result)
        return Response("success")
    except:
        traceback.print_exc()
        return Response("db error")

@api_view(['POST'])
def create_pdf(request):
    fileName = 'pdfTable.pdf'
    pdf = SimpleDocTemplate(fileName,pagesize=letter)    
    query = "SELECT sales.item_code, food.name, sales.quantity, CAST(sales.date AS char) FROM food inner JOIN sales ON food.ITEM_CODE = sales.ITEM_CODE"
    data = mysql_api(query)
    temp = ["Item Code" , "Food name", "Quatity" , "Sale time"]
    data.insert(0,temp)

    # for CSV


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in data:
            writer.writerow(i)

    # for pdf 


    table = Table(data)
    customColor = colors.Color(red=(74.0/255),green=(98.0/255),blue=(255.0/255))
    customColor1 = colors.Color(red=(150.0/255),green=(180.0/255),blue=(255.0/255))
    customColor2= colors.Color(red=(255.0/255),green=(255.0/255),blue=(255.0/255))
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), customColor),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
      
        ('FONTSIZE', (0,0), (-1,0), 14),

        ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ])
    table.setStyle(style)

    rowNumb = len(data)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = customColor1
        else:
            bc = customColor2
        
        ts = TableStyle(
            [('BACKGROUND', (0,i),(-1,i), bc)]
        )
        table.setStyle(ts)

    ts = TableStyle(
        [
        ('BOX',(0,0),(-1,-1),1,colors.black),
        ('GRID',(0,0),(-1,-1),1,colors.black),
        ]
    )
    table.setStyle(ts)
    elems = []
    elems.append(table)
    pdf.build(elems)
    return (response)

@api_view(['POST'])
def get_chart(request):

    if(request.method=='POST'):
        query="select Food.name, sum(quantity) from sales join Food on (Food.item_code = sales.item_code) Where (Food.isvisible = 1) group by sales.item_code"
        x= mysql_api(query)
        labels, data = zip(*x)
        color =  ['rgba(' + str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) + "," + str(random.randint(0, 200)) + ", 0.6)" for _ in range(len(data))]
        return Response({"labels":labels,"datasets":[{"label":"salesreport","data":data, "backgroundColor": color,}]})

@api_view(['POST'])
def getingredient_list(request):
    try:
        if(request.method=='POST'):
            query="select name from inventory"
            result = mysql_api(query)
            result = [i[0] for i in result]
            #print(result)
            return Response(result)
        else:
            return Response("no inventory")
    except:
        traceback.print_exc()


@api_view(['POST'])
def add_food(request):
    try:
        if(request.method=='POST'):
            data=request.data
            ingredientsList = data["nameList"]
            quantityList = data["quantityList"]
            ingredientsdict=dict(mysql_api("select name,ingredient_id from inventory"))
            
            if Food.objects.filter(name=data["foodname"]).exists():
                return Response("food already exists")
            else:
                for i in range(0,len(ingredientsList)):
                    ingredientsList[i] = str(ingredientsdict[ingredientsList[i]])
                visibility=1
                if(int(data["price"])==0):
                    visibility=0
                ingListString = ",".join(ingredientsList)
                ingquantityString=",".join(str(_) for _ in quantityList)
                new_food = Food(name= data["foodname"].upper(),ingredient_list_id=ingListString,quantity_list=ingquantityString,price=data["price"],isvisible=visibility)
                new_food.save()

                return Response("food created")
    except:
        traceback.print_exc()

@api_view(['POST'])
def add_ingredients(request):
    try: 
        if(request.method=='POST'):
            data=request.data["name"]
            print(data)
            if Inventory.objects.filter(name=data).exists():
                return Response([(data + " already exists"),"warning"])
            new_ing=Inventory(name=data,quantity=0)
            new_ing.save()
            return Response(["ingredients created","success"])
    except:
        traceback.print_exc()