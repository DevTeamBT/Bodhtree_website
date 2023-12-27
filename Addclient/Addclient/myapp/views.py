
# Create your views here.
# views.py
from django.shortcuts import render
import mysql.connector as sql
from myapp.models import Add_requirement

COMPANY_NAME=''
URL=''
Address_1=''
Address_2=''
Country=''
State=''
City=''
Zip=''
Industry=''
Company_Size=''
Linkedin=''
Networth=''

def all_events(request):
    forums = Add_requirement.objects.all()
    return render(request,'templates/forums.html',
        {'data': forums})

def Addreq(request):
    data=Add_requirement.objects.all()
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",password="root",database="sales")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='COMPANY_NAME':
                COMPANY_NAME=value
            if key=='URL':
                URL=value
            if key=='Address_1':
                Address_1=value
            if key=='Address_2':
                Address_2=value
            if key=='Country':
                Country=value
            if key=='State':
                State=value
            if key=='City':
                City=value
            if key=='Zip':
                Zip=value
            if key=='Industry':
                Industry=value
            if key=='Company_Size':
                Company_Size=value
            if key=='Linkedin':
                Linkedin=value
            if key=='Networth':
                Networth=value
        c="insert into add_company VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(COMPANY_NAME,URL,Address_1,Address_2,Country,State,City,Zip,Industry,Company_Size,Linkedin,Networth)
        cursor.execute(c)
        m.commit()
        
        with m:
            with m.cursor() as cursor:
                form_data = {key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken'}
                user_instance = Add_requirement(**form_data)
                user_instance.save()
                m.close()
                
        return render(request, 'Addcompany.html', {'data': data})
    return render(request,'Addcompany.html')
        
   
