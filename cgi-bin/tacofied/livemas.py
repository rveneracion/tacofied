#! /usr/bin/python

import tacofy, cgi

form = cgi.FieldStorage()

yourname = form.getvalue('yourname')

#start content
print "Content-Type: text/html\r\n\r\n"

print tacofy.taco_bellify(yourname)
