# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd


def scrape():

    # NASA Mars News
    # ---------------------------------------------------
    # page uses js to load in content so straight bs scrape won't get everything
    # use splinter to open a browser and scrape that
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # establish mars news site url
    url = 'https://redplanetscience.com/'

    # have browser navigate to url
    browser.visit(url)

    # call html from browser
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')

    # find first result for 'content_title' and save the text as a string
    news_title = soup.find('div', class_='content_title').text

    # find first result for 'article_teaser_body' and save the text as a string
    news_p = soup.find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image
    # ---------------------------------------------------
    # establish url for this section
    image_url = 'https://spaceimages-mars.com/'

    # navigate to this page in browser
    browser.visit(image_url)

    # call html from browser
    img_html = browser.html 

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(img_html, 'html.parser')

    # use the beautifulSoup 'find' function to determine the source path for the image
    featured_img_path = soup.find('img', class_='headerimage fade-in')['src']

    # add the image path to the url to find the full url for the featured image
    featured_image_url = image_url + featured_img_path

    # Mars Facts
    # --------------------------------------------------
    # establish url for mars facts page
    facts_url = 'https://galaxyfacts-mars.com/'

    # navigate browser to facts page
    browser.visit(facts_url)

    # call html from browser
    facts_html = browser.html

    # use pandas read_html function to scrape table data from the html
    tables = pd.read_html(facts_html, header=0)

    # store the tables separately
    comparisons_df = tables[0]
    profile_df = tables[1]

    # adjust comparison table formatting
    comparisons_df = comparisons_df.rename(columns={'Mars - Earth Comparison': 'Attribute'})

    # convert the dfs to html table strings
    comparisons_html = comparisons_df.to_html(classes='table table-striped')
    profile_html = profile_df.to_html(classes='table table-striped')

    # Mars Hemispheres
    # -------------------------------------------------
    # establish url for mars hemispheres page
    hemi_url = 'https://marshemispheres.com/'

    # navigate browser to hemispheres page
    browser.visit(hemi_url)

    # call html from browser
    hemi_html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(hemi_html, 'html.parser')

    # find all items in the hemisphere list
    items = soup.find_all('a', class_='itemLink product-item')

    # establish empty lists for links and titles
    links = []

    # iterate through results to find all links
    for item in items:
        # attempt to pull link from item, if there isn't one continue to next iteration
        try:
            link = item['href']
        except:
            continue
        
        # avoid adding duplicates to list of links
        if link not in links:
            links.append(link)
            
    # remove useless link from list
    links.remove('#')

    # create empty list for result dictionaries
    hemisphere_img_urls = []

    # navigate to each subpage to find title and image link
    for link in links:
        sub_url = hemi_url + link
        
        # navigate to subpage
        browser.visit(sub_url)
        
        # call page html
        sub_html = browser.html
        
        # Parse HTML with Beautiful Soup
        soup = bs(sub_html, 'html.parser')
        
        # Find the title on the page
        title = soup.find('h2', class_='title').text
        
        # find the link to the 'Original' image on each page
        href = soup.find('img', class_='wide-image')['src']
        
        # create full image url
        img_result_url = hemi_url + href
        
        # create result dictionary
        hemi_dict = {'title': title, 'img_url': img_result_url}
        
        # append dictionary to list
        hemisphere_img_urls.append(hemi_dict)

    # close browser
    browser.quit()

    # Condense all data into one dictionary
    # -----------------------------------------------------
    data_dict = {'news_title': news_title,
                'news_p': news_p,
                'featured_img_url': featured_image_url,
                'comparisons_html': comparisons_html,
                'profile_html': profile_html,
                'hemisphere_img_urls': hemisphere_img_urls}

    # return final result
    return data_dict