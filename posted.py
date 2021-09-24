#!/usr/bin/env python3
import cgi, cgitb
import secret
    
print ("Content-Type:text/html\r\n\r\n")


form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

user = secret.username
pw = secret.password


if username == user and password == pw:
    # successful login

    #set cookie
    

    print("<html>")
    print("<head>")
    print("<title>Posted</title>")
    print("</head>")
    print("<body>")
    print("<p>username: "+username + ", password: " + password+"</p>")
    print("</body>")
    print("</html>")

else:
    # wrong username/password

    print("<html>")
    print("<head>")
    print("<title>Posted</title>")
    print("</head>")
    print("<body>")
    print("<p> <a href=\"hello.py\"> Try again. </a></p>")
    print("</body>")
    print("</html>")