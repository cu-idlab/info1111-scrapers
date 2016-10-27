#Import Modules
import urllib.request
import re

#Define websites to look through
page1 = "https://www.yelp.com/biz/the-sink-boulder"
page2 = "https://www.yelp.com/biz/the-fat-shack-boulder"

#Define the function used to pull html  
def find_reviews(page):
    web_page = urllib.request.urlopen(page)
    lines = web_page.read().decode(errors="replace")
    #Reviews
    #hits = re.findall('''<p lang="en">(.*?)</p> ''',lines.replace("<br>","").replace("&#39;","'").replace("&#34",'"'))
    #Star Rating
    hits = re.findall('''title="(.*?)star rating">
            <img alt''',lines)
    return hits

print("Searching: ", page2)

#Use find_reviews function to create a list of reviews by sending it a page, name the list reviewlist
reviewlist = find_reviews(page2)

print("Found this many reviews: " + str(len(reviewlist)))
count = 1

#Go through each review in the list and print it
for review in reviewlist:
    print("Review " +str(count)+ ": "+ review +"\n")
    count+=1
