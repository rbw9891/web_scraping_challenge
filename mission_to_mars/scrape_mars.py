# dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# using base: conda enviro
# might need to use it all the time now cause my computer just points to it
# need return at bottom
# need to proof the notebook now too

def scrape():

    # Setup splinter
    # location of driver
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    executable_path = {'executable_path': "C:\\Users\\Reid\\.wdm\\drivers\\chromedriver\\win32\\111.0.5563\\chromedriver.exe"}
    print(executable_path)
    # instantiate browser object, will open a new empty browser window
    browser = Browser('chrome', **executable_path, headless=False)

    # set url to mars news site
    url = "https://redplanetscience.com/"

    # visit webpage with splinter
    browser.visit(url)

    # have splinter grab the html
    # create beautiful soup object from html
    html = browser.html
    soup = bs(html, "html.parser")


    # find the <section class="image_and_description_container" and
    # assign the latest news title and paragraph to variables
    for results in soup.find_all("section", class_="image_and_description_container"):
        news_title = results.find("div", class_="content_title").text
        news_para = results.find("div", class_="article_teaser_body").text

    # set url to space image site and visit page
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    # have splinter grab the html
    # create beautiful soup object from html
    html = browser.html
    soup = bs(html, "html.parser")

    # find image src
    image = soup.find("img", class_="headerimage fade-in")["src"]

    # create variable for image url
    featured_image_url = f"https://spaceimages-mars.com/{image}"

    # mars facts url
    pandas_url = "https://galaxyfacts-mars.com/"

    # read_html method to get tables
    tables = pd.read_html(pandas_url)

    # get the mars/earth comparison table
    mars = tables[0]

    # rename columns
    mars = mars.rename(columns={0:"Description",1:"Mars",2:"Earth"})

    # set index to description column
    mars.set_index(["Description"], inplace=True)

    # write to html string
    mars.to_html("mars_table.html", encoding="utf-8")

    # set url to astrogeology site and visit page
    url = "https://marshemispheres.com/"
    browser.visit(url)

    # set empty list to be appended with dicts
    hemisphere_image_urls = []

    # find the proper div by css and assign to variable item
    item = browser.find_by_css('div[class="description"]')

    # click first link
    item.find_by_tag('h3').click()

    # splinter grab html, create soup object
    html = browser.html
    soup = bs(html, "html.parser")
    # find first li tag, a tag, and href inside a tag
    image_1 = soup.find('li').find('a')['href']

    # find h2 tag, class title and text of that
    title_1 = soup.find('h2', class_='title').text

    # create dict to go into empty list
    hem_1 = {"title":title_1,
        "img_url":f"{url}{image_1}"}

    # splinter navigate back to home page
    browser.back()

    # click second link
    item[1].find_by_tag('h3').click()

    # splinter grab html, create soup object
    html = browser.html
    soup = bs(html, "html.parser")
    # find first li tag, a tag, and href inside a tag
    image_2 = soup.find('li').find('a')['href']
    # find h2 tag, class title and text of that
    title_2 = soup.find('h2', class_='title').text
    # create dict to go into empty list
    hem_2 = {"title":title_2,
            "img_url":f"{url}{image_2}"}

    # splinter navigate back to home page
    browser.back()

    # click third link
    item[2].find_by_tag('h3').click()

    # splinter grab html, create soup object
    html = browser.html
    soup = bs(html, "html.parser")
    # find first li tag, a tag, and href inside a tag
    image_3 = soup.find('li').find('a')['href']
    # find h2 tag, class title and text of that
    title_3 = soup.find('h2', class_='title').text
    # create dict to go into empty list
    hem_3 = {"title":title_3,
        "img_url":f"{url}{image_3}"}

    browser.back()

    # click final link
    item[3].find_by_tag('h3').click()

    # splinter grab html, create soup object
    html = browser.html
    soup = bs(html, "html.parser")
    # find first li tag, a tag, and href inside a tag
    image_4 = soup.find('li').find('a')['href']
    # find h2 tag, class title and text of that
    title_4 = soup.find('h2', class_='title').text
    # create dict to go into empty list
    hem_4 = {"title":title_4,
        "img_url":f"{url}{image_4}"}

    # add dicts to list
    hemisphere_image_urls.extend((hem_1,hem_2,hem_3,hem_4))

    # close splinter browser
    browser.quit()

    scrape_dict = {}

    scrape_dict["News Title"] = news_title
    scrape_dict["News Paragraph"] = news_para
    scrape_dict["Feature Image"] = featured_image_url
    scrape_dict["Hemi Images"] = hemisphere_image_urls


    # return
    print(scrape_dict)

