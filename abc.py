import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
final=''
temp=''
for i in range(1,31):
   a=str(i)
   headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} #To bypass request-blocking from WAF
   respo =requests.get("https://passcomptia.com/comptia-security/comptia-security-question-m-"+a,headers=headers)  # Change the page
   abc=respo.text
   soup= BeautifulSoup(abc, 'html.parser')

   content=soup.find('div',{"class": "entry-content"}) 
   print("Ques."+a+str(content))




