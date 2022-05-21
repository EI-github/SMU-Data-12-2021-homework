import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from IPython.display import display, Image
from datetime import datetime

class HelpScrape():
    def __init__(self):
        pass #no base URL

    def getData(self):
        # Setup splinter INSTEAD
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)

        redplanet_url = "https://redplanetscience.com/"
        browser.visit(redplanet_url)

        html = browser.html
        chicken_noodle = bs(html)

        #scrapes the news titles
        news_title = chicken_noodle.find_all("div", {"class":"content_title"})[0].text

        #scrapes the blurb under the news title
        news_p = chicken_noodle.find_all("div", {"class":"article_teaser_body"})[0].text

        spaceimages_url = "https://spaceimages-mars.com/"
        browser.visit(spaceimages_url)

        html = browser.html
        chicken_noodle = bs(html)

        #scrapes the image URL
        featured_image_url = spaceimages_url + chicken_noodle.find("img", {"class":"headerimage"})["src"]

        galaxyfacts_url = "https://galaxyfacts-mars.com/"
        browser.visit(galaxyfacts_url)

        html = browser.html
        dfs = pd.read_html(html)

        # finds facts table
        df = dfs[1]
        df.columns=["Statistic", "Value"]

        marshemi_url = "https://marshemispheres.com/"
        browser.visit(marshemi_url)

        html = browser.html
        split_pea = bs(html)
        items = split_pea.find_all("div", {"class": "item"})

        hemisphere = []

        for item in items:
            # parse page 1
            item_link = item.find("div", {"class", "description"}).find("a")
            item_url = marshemi_url + item_link["href"] #builds url
            item_title = item_link.text.strip().strip("Enhanced").strip() #strips out title

            # visit the found URL
            browser.visit(item_url)
            html2 = browser.html
            split_pea2 = bs(html2)
            hemi_url = marshemi_url + split_pea2.find("img", {"class": "wide-image"})["src"] #locates image URL

            #throws it all together, used in mongoHelper
            data = {"title": item_title, "img_url": hemi_url}
            hemisphere.append(data)

        data_scraped = {}
        data_scraped["news_p"] = news_p
        data_scraped["news_title"] = news_title
        data_scraped["featured_image_url"] = featured_image_url
        data_scraped["mars_facts"] = df.to_html() #takes df from galaxyfacts and converts to html
        data_scraped["hemispheres"] = hemisphere
        data_scraped["last_updated"] = datetime.now()
        

        browser.quit()

        return(data_scraped)


