import requests
import os
from pypdf import PdfMerger

pageStart= 1
pageEnd = 488
doid = 5657

for page in range(pageStart,pageEnd+1):
    stri = 'https://ilib.mu-pleven.bg/bg/getfile.php?iid=DO-L10000514&doid=' + doid + "&page="
    if(page<10):
        stri+='000'+str(page)
    elif page<100:
        stri+='00'+str(page)
    elif page<1000:
        stri+='0'+str(page)
    else:
        stri+=str(page)
    print(stri)
    x = requests.get(stri)
    with open('temp/'+str(page)+'.pdf', "wb") as f:
        f.write(x.content)
    page+=1

merger = PdfMerger()

for page in range(pageStart,pageEnd+1):
    merger.append('temp/'+str(page)+'.pdf')

merger.write(doid+".pdf")
merger.close()

for page in range(pageStart,pageEnd+1):
    os.remove("temp/"+str(page)+'.pdf')    
