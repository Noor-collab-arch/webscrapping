import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
url =('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
web=requests.get(url)
#print(web.status_code)
soup =BeautifulSoup(web.text,'html')
#print(soup)
title_name = soup.find_all('a',class_="title")
#print(title_name)
for i in title_name:
    print(i.text)
price = soup.find_all('h4', class_="price float-end card-title pull-right")    
for j in price:
    print(j.text)
descrp = soup.find_all('p', class_="description card-text")
for k in descrp:
    print(k.text)


laptops = []
for i, j, k in zip(title_name, price, descrp):
        laptops.append({
            "Title": i.text,
            "Price": j.text,
            "Description": k.text
        })

    # Display the scraped data in a table

st.subheader("Laptops")

for laptop in laptops:
        st.write(f"### {laptop['Title']}")
        st.write(f"**Price:** {laptop['Price']}")
        st.write(f"**Description:** {laptop['Description']}")
        st.write("---")  # Add a divider

else:
    st.error("Failed to retrieve the webpage. Please try again later.")    