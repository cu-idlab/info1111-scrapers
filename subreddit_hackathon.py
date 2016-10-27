'''
SUBREDDIT DATA COLLECTION SCRIPT

This script collects data from reddit about subreddits.
It is a good example of a straight forward piece of code
that contacts reddit servers, collects information, and
stores it in a file on your hard drive.

Sound fun? Let's get started.

'''

# Import python libraries needed to run this code
import requests
import csv
import time
import nltk
from nltk.corpus import stopwords
import pandas as pd
from bs4 import BeautifulSoup
import re
from pprint import pprint


################################################################################
# Define variables that our script needs to run
################################################################################

# How many subreddits do you want to download?
# (CHANGE THIS VARIABLE. kthxbai.)
subreddit_count = 10

# Filename: Where do you want your data saved?
filename = 'reddit_info.tsv'

# Results: This variable is like a "bucket." We will add subreddit data to
# this bucket.
results = []

# This is the web address our script will call. Please don't edit this.
request_url = 'http://www.reddit.com/subreddits.json?limit=1&after='

# User-Agent: This variable is used to make some fancy technical things happen.
# Honestly, it is a little scary and you should feel free to ignore it.
# If you are brave, Google it or ask Jed. But otherwise, move along.
user_agent= {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6'}

# Header:
# This is a list of columns for the data that reddit will return and
# that we will store.
header = ['accounts_active','banner_img', 'banner_size',
'collapse_deleted_comments', 'comment_score_hide_mins', 'created',
'created_utc', 'description', 'display_name', 'header_img', 'header_size',
'header_title', 'hide_ads', 'icon_img', 'icon_size', 'id', 'key_color', 'lang',
'name', 'over18', 'public_description', 'public_description_html',
'public_traffic', 'quarantine', 'show_media', 'show_media_preview',
'submission_type', 'submit_link_label', 'submit_text', 'submit_text_html',
'submit_text_label', 'subreddit_type', 'subscribers', 'suggested_comment_sort',
'title', 'url', 'user_is_banned', 'user_is_banned', 'user_is_contributor',
'user_is_moderator', 'user_is_muted', 'user_is_subscriber',
'user_sr_theme_enabled', 'wiki_enabled']

################################################################################
# Magic Time!
# Let's get data!
#
# This part of the script actually requests data
# from reddit, interprets that data, and adds
# it to the 'results' variable.
################################################################################

# 1. Initialize the 'after_token.'
# The after_token is used to get the next page of data. We'll start on page
# one, so we don't need an after token yet.
after_token = ''

# 2. Request data until we have the amount of data we want.
# This is a 'loop' structure. The way to read this code would be something like:
#   "Until (while) the number of subbreddits in results (len(results)) is
#   less than (<) the number of subreddits we want (subreddit_count)
#   do everything listed below..."
while len(results) < subreddit_count:

    # 3. Contact reddit. Request some data.
    r = requests.get(request_url+after_token, headers=user_agent)

    # 4. Translate it from the JSON format to something more usable
    data = r.json()

    # 5. Get the after_token so we can get more data in the next call
    after_token = data['data']['after']

    # 6. Create a 'dictionary.' This is like a row in a spreadsheet.
    tmp_dict = {}

    # 7. Place data in that dictionary.
    for item in header:
        tmp_dict[item] = str(data['data']['children'][0]['data'][item]).encode('utf-8')

    # 8. Add the dictionary to results -- the bucket where we are putting data.
    results.append(tmp_dict)

    # 9. Now we tell our program to sleep for a nanosecond.
    # This is a considerate thing to do. It also prevents us from looking like
    # we're attacking their site.

    time.sleep(.1)
    # 10. Finally, print out some progress information, and what subreddit
    # we just pulled. Also, programmers are impatient.
    pprint(str(len(results)) + '/' + str(subreddit_count) + ' : ' + str(tmp_dict['url']))

    # Now we're done with this loop. Let's do it again! (Return to #3.)


################################################################################
# Save your data!
# This part of the script takes all of your
# beautiful data and saves it to a file.
################################################################################
with open(filename, 'w') as csvfile:
    fieldnames = results[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for result in results:
        writer.writerow(result)
# That stuff right up there? Kinda magic, and not super important to understand
# right now. Important thing? You're file is done. Go open it in Excel.


################################################################################
# Nice work! You're done.
################################################################################
pprint('Nice work! You\'re done.')
pprint('Now enjoy a cat: http://random.cat/')

'''
Looking for more? There are a couple ways you can build on this code.

1. Look at the subreddit API and find ways to search for specific subbreddits
https://www.reddit.com/dev/api/#section_subreddits

2. Try accessing the front page:
http://www.reddit.com/.json
Pro-tip: Will pages work the same way here?

3. Any page you want! This code is meant to fetch "json" encoded data from
reddit. Most pages on reddit become json if you edit the URL and add ".json"
to the end. That easy enough to let you get into all kinds of trouble.

'''
