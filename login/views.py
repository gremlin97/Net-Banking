from django.shortcuts import render
import mysql
from mysql.connector import Error

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):

    if ('Accno' in request.session):
        return render(request, 'Dashboard.html', {'user': request.session.get('uname') ,'msg': request.session.get("uname"), 'msg1' : 'Sucessfully logged in' , 'msg2': ''})
    else:
        return render(request, 'login.html')
def logout(request):
    request.session.flush()
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def gallery(request):
    return render(request, 'gallery.html')
def services(request):
    return render(request, 'services.html')
def register(request):
    return render(request, 'register.html')

def Dashboard(request):
    if ('Accno' in request.session):
        return render(request, 'Dashboard.html', {'user': request.session.get('uname') ,'msg': request.session.get("uname"), 'msg1' : 'Sucessfully logged in' , 'msg2': ''})
    else:
        return render(request, 'login.html')

def resetpass(request):
    Accno = request.session.get('Accno')
    oldpass = request.POST.get('oldpass')
    newpwd = request.POST.get('newpwd')
    cnewpwd = request.POST.get('cnewpwd')

    if(newpwd == cnewpwd):
        conn = mysql.connector.connect(host="localhost", user='root', password='root', database='kiran')
        cursor = conn.cursor()

        query1 = "SELECT password FROM user_info WHERE Accno = '%d' " % (Accno)
        cursor.execute(query1)
        q1 = cursor.fetchall()
        if(oldpass == q1[0][0]):
            q = "UPDATE user_info SET password=%s WHERE Accno = %d " %(newpwd,Accno)
            cursor.execute(q)
            conn.commit()
            cursor.close()
            conn.close()
            msg = "password sucessfully updated"
            return render(request,"Dashboard.html", {'user': request.session.get("uname"),'msg5': msg})
        else:
            msg = "You entered incorrect password"
            return render(request, "Dashboard.html", {'user': request.session.get("uname"),'msg5': msg})

    else:
        msg = "confirm password doesn't match"
        return render(request, "Dashboard.html", {'user': request.session.get("uname"),'msg5': msg})

def authenticate(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')

    conn = mysql.connector.connect(host="localhost", user='root', password='root', database='kiran')
    cursor = conn.cursor()

    query1 = "SELECT password,Firstname,Accno,Balance,Acctype FROM user_info WHERE username = ('%s')" % (uname)
    cursor.execute(query1)
    q1 = cursor.fetchall()
    if (pwd == q1[0][0]):
        msg = "Sucessfully logged in"
        request.session['Accno'] = q1[0][2]
        request.session['uname'] = uname
        request.session.set_expiry(0)
        user = request.session['uname']
        return render(request, 'Dashboard.html', {"msg": msg, 'user': user})
    else:
        msg = "Password is incorrect"
        return render(request, 'login.html', {"msg": msg})

def valregistration(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    type = request.POST.get('type')
    ia = int(request.POST.get('ia'))
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')

    if (pwd == cpwd):

        conn = mysql.connector.connect(host="localhost", database="kiran", user="root", password="root")
        cursor = conn.cursor()

        q1 = "insert into user_info(Firstname, Lastname, Acctype, Balance, username, password) values ('%s' , '%s', '%s', '%f', '%s','%s')" % (
        fname, lname, type, ia, uname, pwd)

        cursor.execute(q1)
        conn.commit()

        cursor.close()
        conn.close()

        msg = "Succesfully registered"
        return render(request, 'register.html', {'msg': msg})

    else:
        msg = "Password doesn't match"
        return render(request, 'register.html', {'msg': msg})

def transact(request):

    to = int(request.POST.get('to'))
    toname = request.POST.get('toname')
    amount = float(request.POST.get('amount'))
    remarks = request.POST.get('remarks')

    Accno = int(request.session.get('Accno'))
    name = request.session.get('uname')

    conn = mysql.connector.connect(host='localhost', database='kiran', user='root', password='root')
    cursor = conn.cursor()

    q4 = "SELECT Balance From user_info WHERE Accno='%d'" %(Accno)
    cursor.execute(q4)
    list1 = cursor.fetchone()
    FromBal = float(list1[0])
    FromBal=FromBal-amount
    q5 = "SELECT Balance From user_info WHERE Accno='%d'" %(to)
    cursor.execute(q5)
    list2 = cursor.fetchone()
    ToBal = float(list2[0])
    ToBal=ToBal+amount

    q = "UPDATE user_info SET Balance=%f WHERE Accno=%d" %(FromBal, Accno)
    cursor.execute(q)

    q2 = "UPDATE user_info SET Balance=%f WHERE Accno=%d" %(ToBal, to)
    cursor.execute(q2)

    q3 = "INSERT INTO transactions(FromAccno, ToAccno, FromName,ToName,Amount, Remarks) VALUE ('%d','%d','%s','%s','%d','%s')" %(Accno, to, name, toname, amount, remarks)
    cursor.execute(q3)
    conn.commit()
    cursor.close()
    conn.close()
    msg = 'Transaction successfully done.'
    return render(request, 'Dashboard.html', {'msg2': msg , "user" : request.session.get('uname')})

def requestservices(request):
    type = request.POST.get('reqtype')
    remarks = request.POST.get('remarks')
    button = request.POST.get('button')
    Accno = request.session.get('Accno')

    conn = mysql.connector.connect(host='localhost', user='root', password='root', database='kiran')
    cursor = conn.cursor()
    if(button == "submit"):
        query = "INSERT INTO user_requests(UserAccno,ReqType,Remarks) VALUES ('%d','%s','%s')" %(Accno,type,remarks)
        cursor.execute(query)
        conn.commit()
        msg = "Requested Sucessfully"
        return render(request , "Dashboard.html", {'user': request.session.get("uname"),'msg3' : msg})

    if(button == "checkreq"):
        query2 = "SELECT * FROM user_requests WHERE UserAccno = %d "  %(Accno)
        cursor.execute(query2)
        list = cursor.fetchall()
        return render(request , "Dashboard.html", {'user': request.session.get("uname"),'msg3' : list})

    cursor.close()
    conn.close()

def showtransactions(request):
    Accno = request.session.get("Accno")

    conn = mysql.connector.connect(host='localhost', database='kiran', user='root', password='root')
    cursor = conn.cursor()

    q = "SELECT * From transactions WHERE FromAccno='%d'" % (Accno)
    cursor.execute(q)
    list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'Dashboard.html', {"msg4" : list , "user" : request.session.get('uname')})

def checkbal(request):
    Accno = request.session.get('Accno')
    conn = mysql.connector.connect(host='localhost', database='kiran', user='root', password='root')
    cursor = conn.cursor()

    q = "SELECT Balance From user_info WHERE Accno='%d'" % (Accno)
    cursor.execute(q)
    list = cursor.fetchone()
    cursor.close()
    conn.close()
    return render(request , "Dashboard.html", {'msg6' : list[0], 'user' : request.session.get('uname')})

def submitquery(request):
    title = request.POST.get('title')
    query = request.POST.get('query')
    button = request.POST.get('button')
    status = 'pending'
    Accno = request.session.get('Accno')

    conn = mysql.connector.connect(host='localhost', user='root', password='root', database='kiran')
    cursor = conn.cursor()
    if(button == "submit"):
        query1 = "INSERT INTO user_queries(Accno,Title,Query,Status) VALUES ('%d','%s','%s','%s')" % (Accno, title, query,status)
        cursor.execute(query1)
        conn.commit()
        msg = "Submited query Sucessfully"
        return render(request, "Dashboard.html", {'user': request.session.get("uname"),'msg7': msg})

    if(button == "checkquery"):
        query2 = "SELECT * FROM user_queries WHERE Accno = %d " %(Accno)
        cursor.execute(query2)
        list = cursor.fetchall()
        return render(request, "Dashboard.html", {'user': request.session.get("uname"),'msg7': list})

    cursor.close()
    conn.close()

