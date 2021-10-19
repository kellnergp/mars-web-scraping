# web-scraping-challenge

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

Add the image path to the image site url to create the 'featured_image_url'.

Quit the browser.

### Mars Facts

Open a new browser.

Save the Mars Facts site url ('https://galaxyfacts-mars.com/') and visit it with the browser.

Store the site html and use pandas.read_html to search it for html tables, making sure to give the function a header=0 attribute to pull the top row as headers.

Store the two results separately as comparisons_df and profile_df.

Adjust the comparisons_df column names to 'Attribute', 'Mars', and 'Earth'.

Quit the browser.

Use a pandas df.to_html(classes='table table-striped', index=False) function to save each table as an html string.

