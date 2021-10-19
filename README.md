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
