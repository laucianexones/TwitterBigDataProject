#! /usr/bin/python

import getCredentials 


# search the keyword python in english language for 100 times
# write the tweet text to a file, if the tweet contains hashtags, write them
# to the file as well
f = open('search_tr','a')
tweets = getCredentials.api.GetSearch('python',lang='en', count=100)
for t in tweets:
    tweet = t.text
    hashtag = []
    for word in tweet.split():
        if word.startswith('#'):
            hashtag.append(word)
    try:
        f.write('%s\n' % tweet)
        if len(hashtag) > 0:
            for tag in hashtag:
                f.write('%s ' % tag)
                f.write('\n')
        f.write('----\n')
    except UnicodeError:
        continue



f.close()
