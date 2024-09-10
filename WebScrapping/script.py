import requests
page = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
# print(page.status_code) 
# print(page.content) 


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.find_all('p')[1].get_text().strip()) 
# print(soup.find("span",{"class":"mw-page-title-main"}).get_text()) 

page2 = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup2 = BeautifulSoup(page2.content, "html.parser")
table = soup2.find_all('table')[0]
import pandas as pd 
main = pd.read_html(str(table))
df = main[0]
print(df) 