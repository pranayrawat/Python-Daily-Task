from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
r = requests.get(url)
soup = BeautifulSoup(r.content,'html5lib')
table = soup.find('table', class_ = 'wikitable')
# print(type(table))
# print(table)
d = table.find_all('tr')
# print(len(d))

typ = []
mutable = []

for i in d[1:]:
    col = i.find_all('td')
#     print(col)
    if col != []:     
        a = col[0].text.strip()
        b = col[1].text.strip()
    
    typ.append(a)
    mutable.append(b)

# print(len(typ))
# print(len(mutable))
# print(typ)
# print(mutable)

dic = {"Type" : typ, "Mutability" : mutable}
# print(dic)

df = pd.DataFrame(dic,columns = ['Type','Mutability'],index=[i+1 for i in range(len(typ))])
print(df)
