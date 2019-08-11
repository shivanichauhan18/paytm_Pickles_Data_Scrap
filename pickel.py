import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

url="https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.868065800000002&longitude=77.7128736"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

dictionary={}
new_pickel_list=[]
main_data_div=soup.find("div",class_="_3RA-")
for index in main_data_div:
    for i in index:
        try:
            price_data=i.find("div",class_="_1kMS").get_text()

            URL = i.a["href"]
            pickelurl="https://paytmmall.com"+URL

            pickel_name=i.find("div",class_="_2apC").get_text()

            pickel_image_url=i.find("div",class_="_3nWP").img["src"]
        except AttributeError:
            continue
        except TypeError:
            continue

        dictionary["name"]=pickel_name
        dictionary["image"]=pickel_image_url
        dictionary["url"]=pickelurl
        dictionary["price"]=price_data
        new_pickel_list.append(dictionary)
pprint(new_pickel_list)