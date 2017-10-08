#! /usr/bin/python
import urllib2, json
s = urllib2.urlopen("http://www.reddit.com/.json")
c = s.read()
j = json.loads(c)


print "Content-type: text/html\r\n\r\n"

for each in j['data']['children']:
	print each['data']['title'] + '<br />'