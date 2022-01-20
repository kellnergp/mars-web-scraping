# Mars News Scraping

## Overview

This project uses the BeautifulSoup Python library to access a series of informational sites about Mars, collate a selection of information, and present it in an aesthetically pleasing way via a Flask-based dashboard page.

A Jupyter Notebook script was used to develop the web-scraping code which was then assembled into a python function to be called from a Flask app.

The Flask app contains routes to scrape updated information, store the data in a Mongo db using PyMongo, and render the scraped data into an HTML template.

![DashPreview]()

## Tools Used

Python

BeautifulSoup

PyMongo

Flask

# Code Walkthrough

<details>
  <summary>Click to expand!</summary>

## Step 1 - Scraping

Jupyter Notebook: https://github.com/kellnergp/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb

First, import necessary dependencies such as pandas, BeautifulSoup, splinter.Browser, and ChromeDriverManager.

### NASA Mars News

Use ChromeDriverManager to set the executable path and open a browser window.

Save the Mars News site url ('https://redplanetscience.com/') and visit it with the browser.

Use a Browser function to save the html of the page.

Create a BeautifulSoup object with the saved html and an 'html.parser'.

Inspect the BeautifulSoup object to understand the page structure and determine the location of the first news title and its paragraph text.

Use a BeautifulSoup find() function to find the first \<div class='content_title'> and save the text component as 'news_title'.

Use a BeautifulSoup find() function to find the first \<div class='article_teaser_body'> and save the text component as 'news_p'.

Quit the browser.

### JPL Mars Space Images - Featured Image

Open a new browser.

Save the Mars Image site url ('https://spaceimages-mars.com/') and visit it with the browser.

Store the browser page html and use it to create a BeautifulSoup object.

Examine the html structure to determine the featured image source is located in an \<img class='headerimage fade-in'> tag.

Use a find() function to locate the tag in the 'soup' object and save the \['src'] attribute as a string, 'featured_img_path'.

Add the image path to the image site url to create the 'featured_img_url'.

Quit the browser.

### Mars Facts

Open a new browser.

Save the Mars Facts site url ('https://galaxyfacts-mars.com/') and visit it with the browser.

Store the site html and use pandas.read_html to search it for html tables, making sure to give the function a header=0 attribute to pull the top row as headers.

Store the two results separately as comparisons_df and profile_df.

Adjust the comparisons_df column names to 'Attribute', 'Mars', and 'Earth'.

Quit the browser.

Use a pandas df.to_html(classes='table table-striped', index=False) function to save each table as an html string representation of tables.

### Mars Hemispheres

Open a new browser.

Save the Mars Hemispheres site url ('https://marshemispheres.com/') and visit it with the browser.

Store the page's html and use it to create a BeautifulSoup object.

Use a find_all() function on the BS object to find all \<a class='itemLink product-item'> tags and save the search result as a list object, 'items'.

Create an empty list, 'links' to store forthcoming subpage links.

Use a for loop to iterate through every 'item' in the 'items' object.

Within the loop, run a try-except with the try clause attempting to store the \['href'] attribute of the 'item' as 'link and the except clause being a command to 
continue to the next loop iteration.

After the try-except, within the for loop, if 'link' is not in 'links' append 'link' to the list.

Following the conclusion of the loop, remove '#' from the 'links' list.

Create an empty list, 'hemisphere_img_urls', to contain forthcoming dictionaries.

Use a for loop to iterate through each 'link' in 'links'.

Within the for loop, add the 'link' to the hemisphere site url string to to create a url string, 'sub_url' for the subpage.

Navigate the browser to the 'sub_url' and store the site html code.

Use the subpage html to create a BeautifulSoup object.

Search the BS object with find() for a \<h2 class='title> tag and store the text as a string, 'title'.

Search the BS object with find() for a \<h2 class='wide-image'> tag and store the \['src'] attribute as a string, 'href'.

Add the hemisphere site url string and the 'href' string to create a full image url string, 'img_result_url'.

Create a dictionary, 'hemi_dict', with the format {'title': title, 'img_url': img_result_url}.

Append 'hemi_dict' to the list, 'hemisphere_img_urls' and then exit the for loop.

Quit the browser.

## Step 2 - MongoDB and Flask Application

### scrape_mars.py

Script: https://github.com/kellnergp/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py

Create a Python script 'scrape_mars.py'.

Define a function, scrape() which contains the Python code from the Jupyter Notebook from step 1.

Remove the intervening browser close an open commands to use 1 browser throughout the function.

Add a step to condense the results from scraping each site in one dictionary, 'data_dict', with the format:

{'news_title': news_title,
                'news_p': news_p,
                'featured_img_url': featured_img_url,
                'comparisons_html': comparisons_html,
                'profile_html': profile_html,
                'hemisphere_img_urls': hemisphere_img_urls}
                
Return 'data_dict' as the output of the scrape() function.

### Flask App

App Script: https://github.com/kellnergp/web-scraping-challenge/blob/main/Missions_to_Mars/app.py

Create a Python app, 'app.py' and import dependencies including: Flask, render_template, and redirect from flask, PyMongo from flask_pymongo, and the scrape_mars python script from the previous step.

Use standard Flask structure to create an instance of Flask.

Connect to a Mongo database with a PyMongo(app, uri="mongodb://localhost:27017/mars_app") function, stored as 'mongo'.

#### Home Route

Establish a home route at "/" and define a home() function.

Find a data record in the Mongo database by calling mongo.db.collection.find_one() and storing the result as 'mission_data'.

Return a render_template() function that will send 'mission_data' to a template, 'index.html'.

#### Scraping Route

Establish a route at "/scrape" and define a scrape() function.

Within the function, run the scrape_mars.scrape() function and store the result as 'mars_data'.

Use a mongo.db.collection.update({}, mars_data, upsert=True) function to send the new version of the scraped data to the Mongo database.

Return a redirect to the home route "/".

### HTML Template

HTML Script: https://github.com/kellnergp/web-scraping-challenge/blob/main/Missions_to_Mars/templates/index.html

Create an HTML document, 'index.html'.

In the \<head> section, set the meta for the viewport, entitle the page 'Mission to Mars', and link to the Bootstrap stylesheet.

#### \<body>

Set the rest of the content inside a Bootstrap \<div class='container-fluid'> so that it will scale to changing viewport size.

At the top of the container, set a 'jumbotron text-center' class \<div>. 

Within that section, set an \<h1> header reiterating the page title and a Bootstrap button linking to the "/scrape" route of the app with a text indication that clicking it will scrape new data.

The next \<div> within the container is a 'row'.

Within this row is only a \<div class='col-md-12'> which contains an \<h3> sub-header with the text 'Latest Mars News', an \<h4> with text calling the 'news_title' from 
'mission_data', and a \<p> with text pulled from {{ mission_data.news_p }}.

After the first row is closed, set another 'row' \<div>.

Within that row, set two columns; one 'col-md-8' and one 'col-md-4'.

Inside the 'col-md-8', place a \<h3> with the text 'Featured Mars Image' followed by an \<img class='img-fluid'> sourced from mission_data.featured_img_url.

Inside the 'col-md-4', place a \<h3> with the text 'Mars Facts' followed by a Bootstrap \<div class='table-responsive'>.

Within the Bootstrap table, call the comparisons table from 'mission_data' in the form {{ mission_data.comparisons_html | safe }} to let Flask know it is safe to run the external table code.

Create a third \<div class='row'>.

The first thing in row three is a \<h3> tag styled to be center-aligned with the text 'Mars Hemispheres'.

After the header, place a \<hr> tag for the sake of pleasant formatting.

Following the horizontal rule, establish four 'col-md-3' class \<div> tags.

Inside each column, set a Bootstrap card \<div> with a 'card-img top' pulled from 'mission_data.hemisphere_img_urls[num].img_url' and a 'card-title' pulled from 
'mission_data.hemisphere_img_urls[num].title'.

For each column, replace num with 0, 1, 2, and 3 respectively.

Each card image should also have a secondary class of 'img-thumbnail' to scale the images down to fit.

After the columns, created one more \<div class='row> with a \<hr> inside of it for formatting.

## Step 3 - Screenshots

Screenshots were taken of the Flask app running in Google Chrome browser.

Screenshot links:

https://github.com/kellnergp/web-scraping-challenge/blob/main/Missions_to_Mars/Screenshots/screenshot_top.png

https://github.com/kellnergp/web-scraping-challenge/blob/main/Missions_to_Mars/Screenshots/screenshot_bottom.png
  
  </details>
  
## Contact
  
  Galen Kellner: kellnergp@gmail.com
