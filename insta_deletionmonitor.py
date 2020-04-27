import datetime
from glob import glob
from sys import argv
from os import chdir, mkdir
from pathlib import Path
from instaloader import Instaloader, Post, Profile, load_structure_from_file

L = Instaloader()
today = datetime.date.today()

## make sure user passed target name
try:
    TARGET = argv[1]
except IndexError:
    raise SystemExit("Profile name required as argument.")

##download new posts:
for post in Profile.from_username(L.context, TARGET).get_posts():
    L.download_post(post, TARGET)

chdir(TARGET)

##Check to see if history file exists for TARGET
if Path(f"{TARGET}deletionhistory.txt").is_file() == False:
    file = open(f"{TARGET}deletionhistory.txt", "w+")
if Path(f"{TARGET}deletionhistory.txt").is_file() == True:
    file = open(f"{TARGET}deletionhistory.txt", "a")

# Obtain set of posts on HD
offline_posts = set(filter(lambda s: isinstance(s, Post),
                           (load_structure_from_file(L.context, file)
                            for file in (glob('*UTC.json.xz') + glob('*UTC.json')))))
# Obtain set of posts that are currently online
post_iterator = Profile.from_username(L.context, TARGET).get_posts()
online_posts = set(post_iterator)

if offline_posts - online_posts:
    file.write(f"Deleted posts crawled {today}:")
    file.write(" ".join(str(p) for p in (offline_posts - online_posts)))
