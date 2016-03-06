if = open('search_tr','w')
tweets = api.GetSearch('python',lang='en', count=100)
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
