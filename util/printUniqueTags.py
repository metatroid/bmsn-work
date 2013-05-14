#!/usr/bin/python
"""
Simple utility script to print all unique tags used in a Tumblr blog.

Call with the Tumblr API name of the blog you want to get the tags for. So, for
example, to get all tags on the blog at iambradleymanning.tumblr.com, invoke as

    python printUniqueTags.py iambradleymanning

"""
import sys, pytumblr

# Define the API keys for our registered "automation utility" app
# in another file, not in our repository.
f = open('consumer_api_keys')
CONSUMER_KEY = f.readline().strip()
CONSUMER_SECRET = f.readline().strip()

# And define our target.
who = sys.argv[1]

client = pytumblr.TumblrRestClient(CONSUMER_KEY, CONSUMER_SECRET)

# How many blog posts do we have?
num_posts = client.blog_info(who)['blog']['posts']
sys.stderr.write('Total number of blog posts for {0}: {1}\n'.format(who, num_posts))

# Make a set of all the tags we've encountered.
my_tags = set()

# Tumblr's API has a max limit of 20, so we do 20 post chunks.
step = 20
for start in range(0, num_posts, step):
    # Get the first chunk of twenty blog posts.
    sys.stderr.write("Fetching {0}'s blog posts from {1} to {2}\n".format(who, start, start+step))
    response = client.posts(who, offset=start)
    # For each post,
    for i in range(len(response['posts'])):
        # add() all the tags. They'll be add()'ed only if there's no duplication.
        for x in range(len(response['posts'][i]['tags'])):
            my_tags.add(response['posts'][i]['tags'][x])

# Print the tags.
while my_tags:
    print my_tags.pop()
