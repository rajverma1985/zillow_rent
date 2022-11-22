# create a webscaper using bs4 and selenium to do the following:
- find rentals in SAN F area below 3000 dollars, with n bedrooms
- use bs4 to scrape through the results and get the price, location/address and url to that rental
- use selenium to fill google forms
- use one form per listing
- the forms will be or can be turned into sheets (google sheets)

## TODO
NOTE: you need to create a new form in Google Forms.
1. Go to https://docs.google.com/forms/ and create your own form
2. Add 3 questions to the form, make all questions "short-answer"
3. Click send and copy the link address of the form. You will need to use this in your program.
4. Go to this web address on Zillow and see how the website is structured, this is where you'll be scraping the data from

Program Requirements:

Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).

- Create a list of links for all the listings you scraped.
- Create a list of prices for all the listings you scraped.
- Create a list of addresses for all the listings you scraped.
- Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing.
- Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.

