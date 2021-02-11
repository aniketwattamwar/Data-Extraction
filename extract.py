import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.m.wikipedia.org/wiki/List_of_Star_Wars_spacecraft'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(re.compile('^h[1-6]$'))
# for names in soup.find_all("h3"):
    
#     print(names.text.strip())
output = []

def get_names():
    for names in soup.find_all("h3"):
        output.append(names.text.strip())
        
    return output

names_list = get_names()
print("List of all the Names\n")
print(names_list)
# blacklist = [
#     '[document]',
#     'noscript',
#     'header',
#     'html',
#     'meta',
#     'head', 
#     'input',
#     'script',
#     'p',
#     'h1',
#     'h2',
#     'h3',
#     # there may be more elements you don't want, such as "style", etc.
# ]

# for t in text:
#     if t.parent.name not in blacklist:
#         output += '{} '.format(t)

# print(output)