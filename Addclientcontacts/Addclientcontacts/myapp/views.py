
# Create your views here.
# views.py
from django.shortcuts import render
import mysql.connector as sql
from myapp.models import Add_requirement

Select_Company =''
Select_Country=''
Select_State =''
Select_City =''
First_Name =''
Last_Name =''
Job_Title =''
Department =''
Email_Id =''
Mobile_No =''
Linkedin=''
Select_Source =''

def all_events(request):
    forums = Add_requirement.objects.all()
    return render(request,'templates/forums.html',
        {'data': forums})

def Addreq(request):
    global Select_Company, Select_Country, Select_State, Select_City, First_Name, Last_Name, Job_Title, Department, Email_Id, Mobile_No, Linkedin, Select_Source
    data=Add_requirement.objects.all()
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",password="root",database="sales")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='Select_Company':
                Select_Company=value
            if key=='Select_Country':
                Select_Country=value
            if key=='Select_State':
                Select_State=value
            if key=='Select_City':
                Select_City=value
            if key=='First_Name':
                First_Name=value
            if key=='Last_Name':
                Last_Name=value
            if key=='Job_Title':
                Job_Title=value
            if key=='Department':
                Department=value
            if key=='Email_Id':
                Email_Id=value
            if key=='Mobile_No':
                Mobile_No=value
            if key=='Linkedin':
                Linkedin=value
            if key=='Select_Source':
                Select_Source=value
        c="insert into add_client_details VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Select_Company,Select_Country,Select_State,Select_City,First_Name,Last_Name,Job_Title,Department,Email_Id,Mobile_No,Linkedin,Select_Source)
        cursor.execute(c)
        m.commit()
        
        with m:
            with m.cursor() as cursor:
                form_data = {key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken'}
                user_instance = Add_requirement(**form_data)
                user_instance.save()
                m.close()
                
        return render(request, 'Addclient.html', {'data': data})
    return render(request,'Addclient.html')
        
   
