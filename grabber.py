from bs4 import BeautifulSoup
import urllib3
import certifi
import os

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', 
    ca_certs=certifi.where()
)

listurl = "https://pvp.qq.com/web201605/herolist.shtml"

html_doc = http.request("GET",listurl).data.decode("gbk")
# print(html_doc)

soup = BeautifulSoup(html_doc,features="lxml")

heros = soup.select(".herolist > li")
print(heros)
heroname_list = []
for hero in heros:
    imgsrc = hero.find("img").get("src")
    heroname = hero.find("img").get("alt")
    heroname_list.append(heroname)

    print(heroname,imgsrc)

    imgdata = http.request("GET","https:"+imgsrc).data
    with open(os.path.join("img",heroname + ".jpg"),"wb") as f:
        f.write(imgdata)

import json

with open("herolist.json","w",encoding="utf-8") as f:
    f.write(json.dumps(heroname_list,ensure_ascii=False))
