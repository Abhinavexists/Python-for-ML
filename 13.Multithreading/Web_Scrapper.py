'''
Real-World Example: Multithreading for I/O bound Tasks
Scenario: Web Scraping
Web scraping often involoves making numerous network request 
to fetch web pages. These tasks are I/O bound because they spend a lot of 
time waiting for reponses from servers. Multithreading can significantly
improvw the performance by alllowing multiple web pages to be fetched concurrently.
'''



import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/how_to/'

]

def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content ,'html.parser')
    print(f'Fetched: {(len(soup.text))} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All Web Pages Fetched')