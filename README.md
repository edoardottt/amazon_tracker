# amazon_tracker

#### amazon_tracker is a simple web scraper that scrapes every x minutes the price of n items and sends an e-mail if the price falls down over p(price selected by you)

Description :mega:
------

It was develop with bs4, requests, time and smtplib libraries. Opening it, you can see some variables:
  - `headers` = It's your browser setting. You have to insert YOUR browser header. You can find it typing 'my user agent' on internet.
  - `URLS` = It's a list that contains the urls of your tracked items.
  - `dream_price` = It's a list that contains the dream price of i-th element in URLS.
  - `from_email` = It's the e-mail that sends the notification.
  - `to_email` = It's the e-mail that receive the notification.
  - `from_password` = It's the password needed for the from_email.
  - `minutes` = How many minutes between a check and the next.
  
IT WORKS ONLY WITH GMAIL ACCOUNTS

Download :satellite:
------

- `git clone https://github.com/edoardottt/amazon_tracker.git

Usage :computer:
------

1) Download all the repo

2) Type on your browser 'my user agent' and paste the result in the header variable content.

3) Change all the variables you need (from_email, from_password, to_email, URLS, dream_price and minutes). 

4) If you haven't did already, go to https://myaccount.google.com/lesssecureapps and allow it (It's mandatory).

5) Execute the scraper.py file
:zap::zap::zap:

If you liked it drop a :star:
-------

https://www.edoardoottavianelli.it for contact me.

                                                    Edoardo Ottavianelli
      
  
