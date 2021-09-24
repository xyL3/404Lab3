#!/usr/bin/env python3
import cgi, cgitb, os
import secret, login

print ("Content-Type:text/html\r\n\r\n")

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

# get cookie 
for var in os.environ:
    if var == "HTTP_COOKIE":
        pairs = os.environ['HTTP_COOKIE'].split(';')
        for pair in pairs:
            l = pair.split('=')
            if l[0] == 'UserID':
                id = l[1]
            if l[0] == 'Password':
                pw = l[1]


# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

def secret_page(username=None, password=None):
    """
    Returns the HTML for the page visited after the user has logged-in.
    """
    if username is None or password is None:
        raise ValueError("You need to pass both username and password!")

    return login._wrapper("""
    <h1> Welcome, {username}! </h1>

    <p> <small> Pst! I know your password is
        <span class="spoilers"> {password}</span>.
        </small>
    </p>
    """.format(username=escape(username.capitalize()),
               password=escape(password)))


# if id == username and pw == password:
if id == username:
    print(secret_page(username,password))