import requests
import os
from pypdf import PdfMerger

page = 1
pageStart= 1
pageEnd = 1090

for page in range(pageStart,pageEnd):
    stri = 'https://ilib.mu-pleven.bg/bg/getfile.php?iid=DO-L20004944&doid=5296&page='
    if(page<10):
        stri+='000'+str(page)+'%27'
    elif page<100:
        stri+='00'+str(page)
    elif page<1000:
        stri+='0'+str(page)
    else:
        stri+=str(page)
    print(stri)
    x = requests.get(stri)
    with open(str(page)+'.pdf', "wb") as f:
        f.write(x.content)
    page+=1

merger = PdfMerger()

for page in range(pageStart,pageEnd):
    merger.append(str(page)+'.pdf')

merger.write("result.pdf")
merger.close()

for page in range(pageStart,pageEnd):
    os.remove(str(page)+'.pdf')    
