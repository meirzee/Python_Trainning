#!C:\\Users\\meirzee\\AppData\\Local\\Programs\\Python\\Python37\\python.exe

import cgi

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

name = form["name"].value
title = form["title"].value
email = form["email"].value

print ("Name:\t" , name, "<br>" )
print ("Title:\t", title, "<br>" )
print ("E-Mail:\t", email, "<br>")
