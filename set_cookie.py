#!/usr/bin/python
import os, cgi
    
form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

    
print("Set-Cookie:UserID = %s;\r\n" %username)
print("Set-Cookie:Password = %s;\r\n" %password)
print("Content-type:text/html\r\n\r\n")

print("Logged in successfully. Cookie set.")

for var in os.environ:
    if var == "HTTP_COOKIE":
        print(os.environ[var])