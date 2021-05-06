import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager 


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars 


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    collection.drop()

    # Nasa Mars news
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    news_html = browser.html
    news_soup = bs(news_html,'lxml')
    news_title = news_soup.find("div",class_="content_title").text
    news_para = news_soup.find("div", class_="rollover_description_inner").text

    # Featured Images
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)
    featured_image_html = browser.html
    featured_image_soup = bs(featured_image_html,"html.parser")
    image_url = featured_image_soup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']
    base_link = "https:" + featured_image_soup.find('div', class_='featured_image_logo').a['href'].rstrip('/')
    feature_url = base_link + image_url
    featured_image_title = featured_image_soup.find('h1', class_="media_feature_title").text.strip()


    # Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'
    table = pd.read_html(mars_facts_url)
    mars_df = table[0]
    mars_df =  mars_df[['Mars - Earth Comparison', 'Mars']]
    mars_fact_html = mars_df.to_html(header=False, index=False)

    # Mars Hemispheres
    mars_hemps_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemps_url)  
    mars_hemps_html = browser.html 
    mars_hemps_soup = bs(mars_hemps_html,"html.parser") 
    results = mars_hemps_soup.find_all("div",class_='item')
    hemisphere_image_urls = []
    for result in results:
            product_dict = {}
            titles = result.find('h3').text
            end_link = result.find("a")["href"]
            image_link = "https://astrogeology.usgs.gov/" + end_link    
            browser.visit(image_link)
            html = browser.html
            soup= bs(html, "html.parser")
            downloads = soup.find("div", class_="downloads")
            image_url = downloads.find("a")["href"]
            product_dict['title']= titles
            product_dict['image_url']= image_url
            hemisphere_image_urls.append(product_dict)

    browser.quit()
    
    mars_data ={
		'news_title' : news_title,
		'summary': news_para,
        'featured_image': feature_url,
		'featured_image_title': featured_image_title,
		'fact_table': mars_fact_html,
		'hemisphere_image_urls': hemisphere_image_urls,
        'news_url': news_url,
        'jpl_url': featured_image_url,
        'fact_url': mars_facts_url,
        'hemisphere_url': mars_hemps_url,
        }
    collection.insert(mars_data)