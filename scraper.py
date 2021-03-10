# -*- coding: utf-8 -*-
"""
@author: edoardottt
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

URLS = ['https://www.amazon.it/Sony-Fotocamera-Mirrorless-Full-Frame-Intercambiabile/dp/B00FWUDE9W','https://www.amazon.it/dp/B01MTOBPGE']

dream_price = [1700,80]
from_email = 'THE EMAIL THAT SENDS THE MESSAGE'
to_email = 'THE EMAIL THAT RECEIVE THE MESSAGE'
from_password = "THE PASSWORD OF from_email"
minutes = 5 #every how many minutes have to check the prices

def check_price():
    for i in range(len(URLS)):
        page = requests.get(URLS[i],headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text()
        price = soup.find(id="priceblock_ourprice").get_text()
        commaindex = price.index(',')
        converted_price = int(price[0:commaindex])
        if(converted_price < dream_price[i]):
            send_mail(title,price[0:commaindex],i)
    
def send_mail(title,price,i):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    
    server.starttls()
    server.ehlo()
    
    server.login(from_email, from_password)
    
    subject = 'PRICE FELL DOWN!'
    body = title.strip() + '\n' + price + " euros" + '\nCheck the amazon link below!\n' + URLS[i]
    
    msg = f"Subject: {subject} \n\n{body}"
    
    server.sendmail(from_email,to_email,msg)
    print("EMAIL SENT!")
    
    server.quit()
    
while(True):
    check_price()
    time.sleep(60*minutes)
