from turtle import st
from bs4 import BeautifulSoup
import time,csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
r=requests.get(START_URL,verify=False)
#print("hello")

def scrape():
    headers=["V Mag","Proper name","Bayer designation","Distance","Spectral class","Mass","Radius","Luminosity"]
    star_data = []
    for i in range(0, 10):
        soup = BeautifulSoup(r.__dict__, "html.parser")
        for row in soup.find_all("tr"):
            td_tags = row.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 1 :
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
            print(star_data)
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()