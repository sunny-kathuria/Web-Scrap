import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

for questions in range(1,31):
   question_number=str(questions)
   headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} #To bypass request-blocking from WAF
   respo =requests.get("https://passcomptia.com/comptia-security/comptia-security-question-m-"+question_number,headers=headers)  # Change the page
   parsed_reponse=respo.text
   soup= BeautifulSoup(parsed_reponse, 'html.parser')

   content=soup.find('div',{"class": "entry-content"}) 
   print("Ques."+question_number+str(content))




