from django.shortcuts import render
import mysql
from mysql.connector import Error

# Create your views here.
def logout(request):
    request.session.flush()
    return render(request,'index.html')
def emplogin(request):
    return render(request,'emplogin.html')
def dashboard(request):
    if ('EmpId' in request.session):
        return render(request, 'EmployeeDash.html',
                      {'emp': request.session.get('Empuname'), 'msg1': 'Sucessfully logged in'})
    else:
        return render(request, 'emplogin.html')

def empauth(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')

    conn = mysql.connector.connect(host="localhost", user='root', password='root', database='kiran')
    cursor = conn.cursor()

    query1 = "SELECT password,Empname,EmpId FROM emloyee_info WHERE username = ('%s') " % (uname)
    cursor.execute(query1)
    q1 = cursor.fetchall()
    if (pwd == q1[0][0]):
        msg = "Sucessfully logged in"
        request.session['Empuname'] = uname
        request.session['EmpId'] = q1[0][2]
        request.session.set_expiry(0)
        emp = request.session['Empuname']
        return render(request, 'EmployeeDash.html', {"msg": msg, 'emp': emp})
    else:
        msg = "Password is incorrect"
        return render(request, 'emplogin.html', {"msg": msg})

def showrequests(request):
    button = request.POST.get('button')
    conn = mysql.connector.connect(host='localhost', database='kiran', user='root', password='root')
    cursor = conn.cursor()
    if (button == "showrequests"):
        q = "SELECT * From user_requests "
        cursor.execute(q)
        list = cursor.fetchall()
        # dict = {'From Acc no ' : list[0][0] , "To Acc no " : list[0][1], "From " : list[0][2], "To " : list[0][3], "Amount " : list[0][4], 'Remarks ': list[0][5] }

        return render(request, 'EmployeeDash.html', {'emp': request.session.get("Empuname"),"msg2": list})

    if (button == "resolvedrequests"):
        status = 'resolved'
        q2 = "UPDATE user_requests SET Status=('%s') " % (status)
        cursor.execute(q2)
        conn.commit()
        return render(request, 'EmployeeDash.html', {'emp': request.session.get("Empuname"),"msg2": 'Sucessfully submitted'})

    cursor.close()
    conn.close()


def showqueries(request):
    button = request.POST.get('button')

    conn = mysql.connector.connect(host='localhost', database='kiran', user='root', password='root')
    cursor = conn.cursor()
    if(button == "showqueries"):
        q = "SELECT * From user_queries "
        cursor.execute(q)
        list = cursor.fetchall()

        #dict = {'From Acc no ' : list[0][0] , "To Acc no " : list[0][1], "From " : list[0][2], "To " : list[0][3], "Amount " : list[0][4], 'Remarks ': list[0][5] }

        return render(request, 'EmployeeDash.html', {'emp': request.session.get("Empuname"),"msg3" : list})

    if(button=="resolvedqueries"):
        status = 'resolved'
        q2 = "UPDATE user_queries SET Status=('%s') " %(status)
        cursor.execute(q2)
        conn.commit()
        return render(request, 'EmployeeDash.html', {'emp': request.session.get("Empuname"),"msg3" : 'Sucessfully submitted'})

    cursor.close()
    conn.close()