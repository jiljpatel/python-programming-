#Web scraping
import requests
from bs4 import BeautifulSoup
import pandas


amazon_url = "https://www.amazon.in/Columbia-Centre-Sneaker-Black-Orange/dp/B089FDYYST/ref=sr_1_2?qid=1645681934&refinements=p_n_feature_nineteen_browse-bin%3A27064187031&rnid=11301362031&s=shoes&sr=1-2"

req = requests.get(amazon_url)

content = req.content

soup =  BeautifulSoup(content,"html.parsar")

all_shoe =soup.find_all("div",{"class":"instrumentation_wrappers"})
scraped_info = []
for shoe in all_shoe:
    shoe_dict = {}
    shoe_dict["name"] = shoe.find("h1",{"class":"a-size-large a-spacing-none"}).text
    shoe_dict["price"]= shoe.find("div",{"data-cel-widget":"corePrice_desktop"}).text
    shoe_dict["color"]= shoe.find("span",{"class":"selection"}).text

       
    all_features_shoe = shoe.find("div",{"id":"featurebullets"})
    
    features = []
    for f in all_features_shoe.find_all("div",{"id":"featurebullets_feature_div"}):
        features.append(f.find("span",{"class":"a-list-item"}).text.strip())
    shoe_dict["features"] = ','.join(features[:-1])
    scraped_info.append(shoe_dict)
    
 #   print(shoe_name,shoe_price,shoe_color,features)    
 
dataframe = pandas.DataFrame(scraped_info)
dataframe.to_csv("amazon.csv")
 
