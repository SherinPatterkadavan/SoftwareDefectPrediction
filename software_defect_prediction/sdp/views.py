from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from django.shortcuts import render
from lstm_knn import predictfn
# Create your views here.
from sdp.models import *


def loginpg(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def login_post(request):
    un=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=un,password=pswd)
        if ob.type == 'admin':
            ob1=auth.authenticate(username='admin',password='123')
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse('''<script>alert("welcome");window,location="/admin_home"</script>''')
        elif ob.type == 'hr':
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid']=ob.id

            return HttpResponse('''<script>alert("welcome");window,location="/home"</script>''')
        elif ob.type == 'TL':
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("welcome");window,location="/Team_Leader"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid user");window,location="/"</script>''')

    except:
        return HttpResponse('''<script>alert("invalid username or password");window,location="/"</script>''')


@login_required(login_url='/')

def admin_home(request):
    return render(request, 'admin/adminindex.html')
@login_required(login_url='/')


def add(request):
    return render(request, 'admin/add.html')

@login_required(login_url='/')

def add_hr(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    username = request.POST['textfield7']
    password = request.POST['textfield8']

    ob = login_table()
    ob.username = username
    ob.password = password
    ob.type ='hr'
    ob.save()

    ob1 = hr_table()
    ob1.name=name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.Email = email
    ob1.phone_no=phone
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Added");window,location="/manage_hr"</script>''')

@login_required(login_url='/')

def edit_hr(request,id):
    ob=hr_table.objects.get(id=id)
    request.session['tlid']=ob.id
    return render(request, 'admin/edit hr.html',{'val':ob})



@login_required(login_url='/')
def edithr(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']

    ob1 = hr_table.objects.get(id=request.session['tlid'])
    ob1.name = name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.Email = email
    ob1.phone_no = phone
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Edited");window,location="/manage_hr"</script>''')


@login_required(login_url='/')
def delete_hr(request,id):
    ob=hr_table.objects.get(id=id)
    ob1=login_table.objects.get(id=ob.LOGIN.id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully delete");window,location="/manage_hr"</script>''')



@login_required(login_url='/')
def block_tl(request,id):
    ob1=login_table.objects.get(id=id)
    ob1.type="blocked"
    ob1.save()
    return HttpResponse('''<script>alert("Successfully blocked");window,location="/block_unblock"</script>''')
def unblock_tl(request,id):
    ob1=login_table.objects.get(id=id)
    ob1.type="TL"
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Unblocked");window,location="/block_unblock"</script>''')



@login_required(login_url='/')
def manage_hr(request):
    ob = hr_table.objects.all()
    return render(request, 'admin/manage_hr.html',{'val':ob})

@login_required(login_url='/')


def manage_hr_search(request):
    name=request.POST['textfield']
    ob = hr_table.objects.filter(name__icontains=name)
    return render(request, 'admin/manage_hr.html',{'val':ob,'search':name})



@login_required(login_url='/')
def notification(request):
    return render(request, 'admin/notification.html')



@login_required(login_url='/')
def notificationsend(request):
   notifications = request.POST['textfield']
   ob = notification_table()
   ob.notifications = notifications
   ob.date=datetime.today()
   ob.save()
   return HttpResponse('''<script>alert("Sent");window,location="/admin_home"</script>''')



@login_required(login_url='/')
def result(request):
    return render(request, 'admin/result.html')



@login_required(login_url='/')
def viewcomplaints(request):
    ob=complaint_table.objects.all()
    return render(request, 'admin/viewcomplaints.html',{'val':ob})



@login_required(login_url='/')
def reply(request,id):
    ob=complaint_table.objects.get(id=id)
    request.session['cid']=ob.id
    return render(request, 'admin/sendreply.html',{'val':ob})



@login_required(login_url='/')
def add_reply(request):
    reply=request.POST['textfield']
    ob=complaint_table.objects.get(id=request.session['cid'])
    ob.replay=reply
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Sent reply");window,location="/viewcomplaints"</script>''')



@login_required(login_url='/')
def viewperformance(request):
    ob=report_table.objects.all()
    return render(request, 'admin/viewperformance.html',{'val':ob})



@login_required(login_url='/')
def viewworkstatus(request):
    ob=work_table.objects.all()
    return render(request, 'admin/viewworkstatus.html',{'val':ob})



@login_required(login_url='/')
#_________________________________________HR_________________________________________________________________________________

def add1(request):
    return render(request, 'hr/add tl.html')



@login_required(login_url='/')
def add_tl(request):
    name = request.POST['textfield']
    place = request.POST['textfield8']
    post = request.POST['textfield7']
    pin = request.POST['textfield6']
    phone = request.POST['textfield5']
    email = request.POST['textfield4']
    username = request.POST['textfield3']
    password = request.POST['textfield2']

    ob = login_table()
    ob.username = username
    ob.password = password
    ob.type ='TL'
    ob.save()

    ob1 = tl_table()
    ob1.name=name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.HR = hr_table.objects.get(LOGIN__id=request.session['lid'])
    ob1.Email = email
    ob1.phone_no=phone
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Added");window,location="/manage_tl"</script>''')



@login_required(login_url='/')
def edit_tl(request,id):
    ob=tl_table.objects.get(id=id)
    request.session['hid']=ob.id
    return render(request, 'hr/edit tl.html',{'val':ob})



@login_required(login_url='/')
def edittl(request):
    print(request.POST)
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']

    ob1 = tl_table.objects.get(id=request.session['hid'])
    ob1.name = name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.email = email
    ob1.phone_no = phone
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Edited");window,location="/manage_tl"</script>''')



@login_required(login_url='/')
def delete_tl(request,id):
    ob=tl_table.objects.get(id=id)
    ob1=login_table.objects.get(id=ob.LOGIN.id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully delete");window,location="/manage_tl"</script>''')



@login_required(login_url='/')
def addwork(request):
    ob=tl_table.objects.all()
    return render(request, 'hr/add work.html',{'val':ob})



@login_required(login_url='/')
def add_work(request):
        print(request.POST)
        TL = request.POST['select']
        work_name = request.POST['textfield2']
        description = request.POST['textfield3']
        deadline = request.POST['textfield4']
        date = request.POST['textfield5']
        status = request.POST['textfield6']

        ob2 = work_table()
        ob2.TL = tl_table.objects.get(id=TL)
        ob2.work_name = work_name
        ob2.description = description
        ob2.deadline = deadline
        ob2.date = date
        ob2.status = status
        ob2.HR=hr_table.objects.get(LOGIN__id=request.session['lid'])
        ob2.save()

        return HttpResponse('''<script>alert("Successfully Added");window,location="/work_assign_to_tl"</script>''')


@login_required(login_url='/')
def block_unblock(request):
    ob = tl_table.objects.filter(HR__LOGIN__id=request.session['lid'])
    return render(request,'hr/block unblock.html',{'val':ob})



@login_required(login_url='/')
def home(request):
        return render(request, 'hr/hrindex.html')


@login_required(login_url='/')
def manage_tl(request):
    ob = tl_table.objects.filter(HR__LOGIN__id=request.session['lid'])
    return render(request, 'hr/manage tl.html', {'val': ob})

@login_required(login_url='/')
def manage_tl_search(request):
    name=request.POST['textfield']
    ob = tl_table.objects.filter(name__icontains=name)
    return render(request, 'hr/manage tl.html',{'val':ob,'search':name})



@login_required(login_url='/')
def viewperformance1(request):
    ob=report_table.objects.all()
    return render(request, 'hr/viewperformance1.html',{'val':ob})



@login_required(login_url='/')
def notification1(request):
    ob=notification_table.objects.all()
    return render(request, 'hr/notification.html',{"val":ob})


@login_required(login_url='/')
def work_assign_to_tl(request):
    ob=work_table.objects.filter(HR__LOGIN__id=request.session['lid'])
    return render(request, 'hr/work asign to tl.html',{'val':ob})



@login_required(login_url='/')
def work_assign_to_tl_search(request):
    name = request.POST['textfield']
    ob = work_table.objects.filter(TL__name__icontains=name)
    return render(request, 'hr/work asign to tl.html',{'val':ob})



@login_required(login_url='/')
def delete_work(request,id):
    ob=work_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Successfully delete");window,location="/work_assign_to_tl"</script>''')



@login_required(login_url='/')
def result1(request):
    return render(request, 'hr/result.html')



@login_required(login_url='/')
#__________________TL_________#

def assign_work_to_tm(request):
    print(request.session['lid'],"------------------------------")
    ob=tm_table.objects.filter(TL__LOGIN__id=request.session['lid'])
    oj=work_table.objects.filter(TL__LOGIN__id=request.session['lid'])
    return render(request, 'tl/assign_work_to_tm.html',{'val':ob,'val1':oj})


@login_required(login_url='/')
def add_work1(request):
    print(request.POST)
    TM = request.POST['select']
    work_name = request.POST['select1']
    details = request.POST['textfield3']
    date = request.POST['textfield5']


    ob2 = assign_table()
    ob2.TM = tm_table.objects.get(id=TM)
    ob2.WORK = work_table.objects.get(id=work_name)
    ob2.work_details = details
    ob2.date = date
    ob2.status = "assigned"
    ob2.TL = tl_table.objects.get(LOGIN__id=request.session['lid'])
    ob2.save()

    return HttpResponse('''<script>alert("Successfully Added");window,location="/Team_Leader"</script>''')



@login_required(login_url='/')
def block_unblock1(request):
    ob=tm_table.objects.all()
    return render(request, 'tl/block_unblock.html',{'val':ob})


@login_required(login_url='/')
def block_tm(request,id):
    ob1=login_table.objects.filter(TL__LOGIN__id=request.session['lid'])
    ob1.type="blocked"
    ob1.save()
    return HttpResponse('''<script>alert("Successfully blocked");window,location="/block_unblock1"</script>''')


@login_required(login_url='/')
def unblock_tm(request,id):
    ob1=login_table.objects.get(id=id)
    ob1.type="TM"
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Unblocked");window,location="/block_unblock1"</script>''')



@login_required(login_url='/')
def Team_Leader(request):
    return render(request, 'tl/tlindex.html')



@login_required(login_url='/')
def update_work_status(request):
    ob = assign_table.objects.all()
    return render(request, 'tl/update_work_status.html', {'val': ob})



@login_required(login_url='/')
def updatework(request,id):
    request.session['pp']=id
    return render(request,"tl/updateworkstatus.html")



@login_required(login_url='/')
def updateworkstatus(request):
   status = request.POST['textfield']
   ob = work_table.objects.get(id=request.session['pp'])
   ob.date=datetime.today()
   ob.status=status
   ob.save()
   return HttpResponse('''<script>alert("Sent");window,location="/Team_Leader"</script>''')



@login_required(login_url='/')
def view_doubt_reply(request):
    ob=doubt_table.objects.filter(TM__TL__LOGIN__id=request.session['lid'])
    return render(request, 'tl/view_doubt_reply.html',{"val":ob})



@login_required(login_url='/')
def view_reportandupd_continous(request):
    ob=report_table.objects.all()
    return render(request, 'tl/view_report&upd_continuos.html',{'val':ob})



@login_required(login_url='/')
def view_reportandupdate(request):
    return render(request, 'tl/view_report&update.html')

@login_required(login_url='/')
def View_teamMember_manage(request):
    ob=tm_table.objects.filter(TL__LOGIN__id=request.session['lid'])
    return render(request, 'tl/View_teamMember_manage.html',{'val':ob})


@login_required(login_url='/')
def View_Work(request):
    ob=work_table.objects.all()
    return render(request, 'tl/View_Work.html',{'val':ob})


@login_required(login_url='/')
def add_tm1(request):
    return render(request, 'tl/add tm.html')



@login_required(login_url='/')
def add_tm(request):
    name = request.POST['textfield']
    place = request.POST['textfield8']
    post = request.POST['textfield7']
    pin = request.POST['textfield6']
    phone = request.POST['textfield5']
    email = request.POST['textfield4']
    username = request.POST['textfield3']
    password = request.POST['textfield2']

    ob = login_table()
    ob.username = username
    ob.password = password
    ob.type ='TM'
    ob.save()

    ob1 = tm_table()
    ob1.name=name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.email = email
    ob1.phone_no=phone
    ob1.LOGIN=ob
    ob1.TL=tl_table.objects.get(LOGIN_id=request.session['lid'])
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Added");window,location="/View_teamMember_manage"</script>''')


@login_required(login_url='/')
def notificationn(request):
    ob=notification_table.objects.all()
    return render(request, 'tl/notificationn.html',{"val":ob})

@login_required(login_url='/')
def edit_tm(request,id):
    ob=tm_table.objects.get(id=id)
    request.session['hid']=ob.id
    return render(request, 'tl/edit tm.html',{'val':ob})


@login_required(login_url='/')
def edittm(request):
    print(request.POST)
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']

    ob1 = tm_table.objects.get(id=request.session['hid'])
    ob1.name = name
    ob1.place = place
    ob1.post = post
    ob1.pin = pin
    ob1.email = email
    ob1.phone_no = phone
    ob1.save()
    return HttpResponse('''<script>alert("Successfully Edited");window,location="/View_teamMember_manage"</script>''')



@login_required(login_url='/')
def delete_tm(request,id):
    ob=tm_table.objects.get(id=id)
    ob1=login_table.objects.get(id=ob.LOGIN.id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully delete");window,location="/View_teamMember_manage"</script>''')



@login_required(login_url='/')
def reply1(request,id):
    ob=doubt_table.objects.get(id=id)
    request.session['did']=id
    return render(request, 'tl/sendreplly.html',{'val':ob})



@login_required(login_url='/')
def add_reply1(request):
    reply=request.POST['textfield']
    ob=doubt_table.objects.get(id=request.session['did'])
    ob.replay=reply
    ob.save()
    return HttpResponse('''<script>alert("Sent reply");window,location="/view_doubt_reply"</script>''')

#---------------------------------------webservices------------------------------------
import  json


def and_login(request):
    un = request.POST['uname']
    pswd = request.POST['password']
    try:
        ob = login_table.objects.get(username=un, password=pswd)
        data={"task":"valid","lid":ob.id}
        r=json.dumps(data)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        return HttpResponse(r)


def and_viewmywork(request):
    tmlid = request.POST['lid']
    ob = assign_table.objects.filter(TM__LOGIN__id=tmlid)
    data=[]
    for i in ob:
        row={"work":i.WORK.work_name, "description": i.WORK.description,"date":str(i.date),"status":i.status,'id':i.id
             }
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)

def and_viewworkreport(request):
    tmlid = request.POST['lid']
    ob = report_table.objects.filter(TM__LOGIN=tmlid)
    data=[]
    for i in ob:
        row={"work":i.ASSIGN.WORK.work_name, "workdetails": i.ASSIGN.WORK.work_details,"report":i.report,"date":i.date,"status":i.status}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)

def and_viewnotification(request):
    ob = notification_table.objects.all()
    data=[]
    for i in ob:
        row={"notification":i.notifications,"date":str(i.date)}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)

def and_viewreply(request):
    tmlid = request.POST['lid']
    ob = complaint_table.objects.filter(TM__LOGIN__id=tmlid)
    data=[]
    for i in ob:
        row={"complaint":i.complaint_details,"date":str(i.date),"reply":i.replay}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)


def and_sendcomplaint(request):
    tmlid = request.POST['lid']
    complaint = request.POST['complaint']

    ob = complaint_table()
    ob.complaint_details=complaint
    ob.date=datetime.now()
    ob.replay="pending"
    ob.TM=tm_table.objects.get(LOGIN__id=tmlid)
    ob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)



def and_updateworkreport(request):
    assinid = request.POST['assinid']
    report = request.POST['report']
    status = request.POST['status']

    ob = report_table()
    ob.report=report
    ob.status=status
    ob.date=datetime.now()
    ob.ASSIGN=assign_table.objects.get(id=assinid)
    ob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)

def and_prediction(request):
    assinid = request.POST['assinid']                             

    ob = result_table()
    ob.allocation= allocation()
    ob.prediction_result=result
    ob.ASSIGN=assign_table.objects.get(id=assinid)
    ob.save()

    data = {"task": "valid"}
    r = json.dumps(data)
    return HttpResponse(r)



def features(request):
    return render(request, 'tl/features.html')


def featurespost(request):
    inputfile=request.FILES['textfield8']
    fs=FileSystemStorage()
    fn=fs.save(inputfile.name,inputfile)
    f = open(fn, "r")


    res=f.read().split(',')
    print(res,"!!!!!!!!!!!!!!!!!!")
    print(res,"!!!!!!!!!!!!!!!!!!")
    print(res,"!!!!!!!!!!!!!!!!!!")
    print(res,"!!!!!!!!!!!!!!!!!!")
    print(res,"!!!!!!!!!!!!!!!!!!")
    print(res,"!!!!!!!!!!!!!!!!!!")
    row=[]
    for i in res:
        row.append(float(i))
    # row=[float(inputfile)]
    res=predictfn(row)
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    print(res,"++++++++++++++++++++++++++++++++++++++++++")
    return render(request,'tl/view.html',{"val":res})

