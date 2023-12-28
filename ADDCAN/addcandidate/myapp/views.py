
# Create your views here.
# views.py
from django.shortcuts import render
import mysql.connector as sql
from myapp.models import Add_requirement


requirement=''
client=''
contact=''
accountmgr=''
candidatename=''
currentcompany=''
mobileno=''
emailid=''
currentctc=''
expectedctc=''
noticeperiod=''
locationpreference=''
location=''
hiretype=''
worktype=''
recruiter=''
selAccmanager=''
position=''

def all_events(request):
    forums = Add_requirement.objects.all()
    return render(request,'templates/forums.html',
        {'data': forums})

def Addreq(request):
    data=Add_requirement.objects.all()
    # for a in addreqData:
    #     print(a.location)
    # print(Addreq)
    # global client,contact,title_for_req,priority,skillsets,must_have,good_to_have,exp_range_min,max,budget_min,budget_max,positions,location,hire_type,work_type,recruiter,account_mgr
    # data={
    #     'addreqData':addreqData
    # }
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",password="rootuser@5168",database="bodhtree1")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="requirement":
                requirement=value
            if key=="client":
                client=value
            if key=="contact":
                contact=value
            if key=="accountmgr":
                accountmgr=value
            if key=="candidatename":
                candidatename=value
            if key=="currentcompany":
                currentcompany=value
            if key=="mobileno":
                mobileno=value
            if key=="emailid":
                emailid=value 
            if key=="currentctc":
                currentctc=value
            if key=="expectedctc":
                expectedctc=value 
            if key=="noticeperiod":
                noticeperiod=value
            if key=="locationpreference":
                locationpreference=value 
            if key=="position":
                position=value
            if key=="location":
                location=value 
            if key=="hiretype":
                hiretype=value
            if key=="worktype":
                worktype=value 
            if key=="recruiter":
                recruiter=value
            if key=="selAccmanager":
                selAccmanager=value
        c="insert into add_candidate values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(requirement,client,contact,accountmgr,candidatename,currentcompany,mobileno,emailid,currentctc,expectedctc,noticeperiod,locationpreference,location,hiretype,worktype,recruiter,selAccmanager,position)
        cursor.execute(c)
        m.commit()
        
        with m:
            with m.cursor() as cursor:
                form_data = {key: request.POST[key] for key in request.POST if key != 'csrfmiddlewaretoken'}
                user_instance = Add_requirement(**form_data)
                user_instance.save()
                
        return render(request, 'addrequirement.html', {'data': data})
    return render(request,'addrequirement.html')
        
    #     "client":client,
    #     "contact":contact,
    #     "title_for_req":title_for_req,
    #     "priority":priority,
    #     "skillsets":skillsets,
    #     "must_have":must_have,
    #     "good_to_have":good_to_have,
    #     "exp_range_min":exp_range_min,
    #     "max":max,
    #     "budget_min":budget_min,
    #     "budget_max":budget_max,
    #     "positions":positions,
    #     "location":location,
    #     "hire_type":hire_type,
    #     "work_type":work_type,
    #     "recruiter":recruiter,
    #     "account_mgr":account_mgr
    # } )
    
    
# views.py
# from django.shortcuts import render
# from .models import Add_requirement

# def retrieve_data(request):
#     data = Add_requirement.objects.all()
#     return render(request, 'myapp/forums.html', {'data': data})
