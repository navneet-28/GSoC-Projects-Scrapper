import requests
import pandas as pd
import bs4

base_url = "https://summerofcode.withgoogle.com/api/program/current/project/?page={}&page_size=50"

example = requests.get(base_url.format(1))

pages = int(example.json()["count"]/50) + 1

main_list = []


for n in range(1,pages+1):
    res = requests.get(base_url.format(n))
    jsonRes = res.json()
    
    for i in range(0,len(res.json()["results"])):
        sub_list = []
        sub_list.append((n-1)*50 + i + 1)
        sub_list.append(jsonRes["results"][i]["title"])
        sub_list.append(jsonRes["results"][i]["student"]["display_name"])
        sub_list.append(jsonRes["results"][i]["organization"]["name"])
        sub_list.append(jsonRes["results"][i]["organization"]["website_url"])
        
        main_list.append(sub_list)
        
df = pd.DataFrame(main_list, columns=["S.No","Project Title","Student","Organization","Website URL"])

df.to_csv('sample_result.csv',index=False, sep=",")