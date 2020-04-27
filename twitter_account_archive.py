import twint
from sys import argv
from os import chdir, mkdir, path

# make sure user passed target name
try:
    TARGET = argv[1]
except IndexError:
    raise SystemExit("Username required as argument.")

c = twint.Config()
c.Username = f'{TARGET}'
c.Store_object = True
c.User_full = True
c.Hide_output = True

#get data
twint.run.Search(c)
target_tweets = twint.output.tweets_list
twint.run.Following(c)
target_following = twint.output.users_list
twint.run.Followers(c)
target_followers = twint.output.users_list
twint.run.Favorites(c)
target_likes = twint.output.tweets_list

# write CSVs
if not path.exists(f'{TARGET}_twitter'):
    mkdir(f'{TARGET}_twitter')
    chdir(f'{TARGET}_twitter')
else:
    chdir(f'{TARGET}_twitter')

with open(f'{TARGET}_tweets.csv', 'w') as output:
    output.write('id,username,date,time,timezone,tweet,mentions,link\n')
    for tweet in target_tweets:
        output.write('{},{},{},{},{},{},{},{}\n'.format(tweet.id, tweet.username, tweet.datestamp, tweet.timestamp, tweet.timezone, tweet.tweet, tweet.mentions, tweet.link))

with open(f'{TARGET}_followers.csv', 'w') as output:
    output.write('id,name,username,bio,location,url\n')
    for user in target_followers:
        output.write('{},{},{},{},{},{}\n'.format(user.id, user.name, user.username, user.bio, user.location, user.url))

with open(f'{TARGET}_following.csv', 'w') as output:
    output.write('id,name,username,bio,location,url\n')
    for user in target_following:
        output.write('{},{},{},{},{},{}\n'.format(user.id, user.name, user.username, user.bio, user.location, user.url))

with open(f'{TARGET}_likes.csv', 'w') as output:
    output.write('id,username,date,time,timezone,tweet,mentions,link\n')
    for tweet in target_likes:
        output.write('{},{},{},{},{},{},{},{}\n'.format(tweet.id, tweet.username, tweet.datestamp, tweet.timestamp, tweet.timezone, tweet.tweet, tweet.mentions, tweet.link))
