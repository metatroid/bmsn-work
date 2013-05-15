#!/usr/bin/python
"""
Simple utility script to download all photos used in a Tumblr blog.

Call with the Tumblr API name of the blog you want to get the photos for. So, for
example, to get all photos on the blog at iambradleymanning.tumblr.com, invoke as

    python downloadPhotos.py iambradleymanning

"""
import sys, os, pytumblr, urllib

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

# Make a set of all the photos we've encountered.
my_photo_urls = set()

# Tumblr's API has a max limit of 20, so we do 20 post chunks.
step = 20
for start in range(0, num_posts, step):
    # Get the first chunk of twenty blog posts.
    sys.stderr.write("Fetching {0}'s blog posts from {1} to {2}\n".format(who, start, start+step))
    response = client.posts(who, offset=start)
    # For each post,
    for i in range(len(response['posts'])):
        # if this post is a photo,
        if 'photo' == response['posts'][i]['type']:
            # TODO: Tumblr provides some EXIF data itself, can we use it?
            # add() the original URL of each photo (if there's no duplication).
            for x in range(len(response['posts'][i]['photos'])):
                my_photo_urls.add(response['posts'][i]['photos'][x]['original_size']['url'])

# Create a directory to store downloaded images.
if False == os.path.isdir(who):
    os.mkdir(who)

# Download all the images.
# TODO: This could use some cleanup.
image = urllib.URLopener()
while my_photo_urls:
    url = my_photo_urls.pop()
    sys.stderr.write("Retrieving image at {0}...\n".format(url))
    file = who + '/' + os.path.basename(url)
    if False == os.path.exists(file):
        try:
            image.retrieve(url, file)
        except Exception:
            sys.stderr.write("Error retrieving image at {0}.\n".format(url))
