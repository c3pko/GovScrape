This project was built off of a Django example with Scrapy under the hood for WikiNews called django-dynamic-scraper.
It is intended to scrape govtrack, archives.gov, any site that has legislative requirements for the The EOP's statutory groups.
You may find it easier to scrape this project and just use a python one-off-command, 
you'll just need to load the python command into a template in order to view it which can be tricky.

As it stands now, the scraper is able to scrape the front page of govtrack.us, it’s able to 
display the name and url of the enacted legislation, and provides a “comment” form for users
to communicate about how to delegate the actions requested by the statutory text or executive 
order text. However, there is no flow of logic within the program and it’s scraping ability is 
not scaled currently to process hundreds of legislative texts.

The most pressing issues are authentication and scraping. The logic flow (HttpResponseRedirect(ing) 
from one url to another based off of user permissions can be easily added after authentication and 
the scraping spider is fixed).

Specifically, currently the url(r’^$’) (the front page) has a “Salutations” windows with a prompt 
for a username and password but no logic to authenticate the user’s id and password as valid, it 
just auto redirects to the /admin page regardless of what is entered.

In the admin page the scraper “GovScrape” and “Gov” don’t follow all of the links on the pages 
fed to them properly. If you click on one of the scrapers and scroll down to “XPATH” there are 
base, url, description, and title element attributes described which follow exactly one link on 
the search.archives OSTP federal register website (specified in News Website).

Suggestions: To help find XPATHs base, url, thumbnail, title, desc element attributes I used 
XPATH Helper which is a chrome add on, if there is a better method for iterating over all 
the urls on the page, use it to get the XPaths instead.

To implement this project: 1) fix the scraper spider, 2) implement authentication through 
a UserForm, 3) implement logic for displaying comments.
