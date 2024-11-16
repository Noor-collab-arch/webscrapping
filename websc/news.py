import requests
from bs4 import BeautifulSoup
url =('https://www.fairobserver.com/latest-updates/?gad_source=1&gclid=Cj0KCQiAouG5BhDBARIsAOc08RT4qiT9hVhESplmT1DnEDSg4ryvj20jsCmRRYBoTR0MJ60U4kYyuD4aAojzEALw_wcB#')
web=requests.get(url)
#print(web.status_code)

soup =BeautifulSoup(web.text,'html.parser')

title_name = soup.find_all('a',class_="fo-post-content")
print(title_name)
'''
for i in title_name:
    print(i.text)
'''