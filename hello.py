#!/usr/bin/env python3
import os, json
import login, templates
print ("Content-Type:text/html\r\n\r\n")
print
print("<title>Test CGI</title>")

#1
# print(os.environ)
# json_object = json.dumps(dict(os.environ), indent = 4)
# print(json_object)

#2
# for var in os.environ:
#     if var == "QUERY_STRING":
#         print(os.environ[var])

# print("<br>")

#3
# for var in os.environ:
#     if var == "HTTP_USER_AGENT":
#         print(os.environ[var])


        
#4
# print(login.login_page())


#5
# print(login.login_cookie())


#6
print(login.login_secret())
