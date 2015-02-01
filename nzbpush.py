#!/usr/bin/python

import httplib, urllib, sys

title = "" #"Download of " + sys.argv[3] + " "
message = "" #"Download of " + sys.argv[3] + " "
serverurl = "http://TKTKTK.local:8080/sabnzbd/"

print("Converting argument " + sys.argv[7] + " to status.")
if(int(sys.argv[7]) == 0):
        title = "Download completed!"
elif(int(sys.argv[7]) == 1):
        title = "Verification failed."
elif(int(sys.argv[7]) == 2):
        title = "Unpacking failed."
elif(int(sys.argv[7]) == 3):
        title = "Verification and unpacking failed."

print("Converting argument " + sys.argv[7] + " to status.")
if(int(sys.argv[7]) == 0):
        message = "Download of " + sys.argv[3] + " has been completed."
elif(int(sys.argv[7]) == 1):
        message = "Verification of " + sys.argv[3] + " failed."
elif(int(sys.argv[7]) == 2):
        message = "Unpacking of " + sys.argv[3] + " failed."
elif(int(sys.argv[7]) == 3):
        message = "Verification and unpacking of " + sys.argv[3] + " failed."

print("Establishing http connection.")
conn = httplib.HTTPSConnection("api.pushover.net:443")
print("Handling request.")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "TKTKTK",
    "user": "TKTKTK",
    "title": title,
    "message": message,
    "url": serverurl,
    "url_title": "Visit web interface",
  }), { "Content-type": "application/x-www-form-urlencoded" })
print("Waiting for response.")
conn.getresponse()
print("Notification send.")
