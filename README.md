# Social Media Collections, or, Every Man His Own SIGINT Agency

Various scripts for archiving and monitoring social media.  Updated as I make more things.

- [Instagram](##Instagram)
- [Twitter](##Twitter)

##Instagram

All scripts will accept multiple inputs.  Based on the [Instaloader](https://github.com/instaloader/instaloader) Python 3.7 module.  To get Instaloader, run:

```
$ pip3 install instaloader
```

###insta_deletionmonitor.py

Coded in a fit of rage when I went to cite a photo in a geolocation only to discover that target had nuked his whole Insta, Instaspy will scrape posts from a target account, check previously archived posts against the online account at time of download, and output a text file listing any previously archived posts that the target has deleted.

```
$ python3 insta_deletionmonitor.py USERNAME
```
or add to crontab. `USERNAME` is a username minus @ symbol. The list of deletions is stored as `{USERNAME}deletionhistory.txt`.

###insta_hashtaggers.py

Outputs username, account link, and ID for all users posting in a hashtag.  Does NOT archive posts.

```
$ python3 hashtaggers.py HASHTAG
```
`HASHTAG` is a hashtag minus # symbol.  Data stored as `{HASHTAG}-taggers.csv`

##Twitter

All scripts will accept multiple inputs.  Based on [Twint](https://github.com/twintproject/twint).  To get Twint, run:

```
$ pip3 install twint
```

###twitter_account_archive.py

Returns tweets including replies, followers, following, and likes for a Twitter user.

```
$ python3 twitter_account_archive.py USERNAME
```
`USERNAME` is a username minus @ symbol. The lists are stored as CSV files in a new directory `{USERNAME}_twitter`.
