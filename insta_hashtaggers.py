import datetime
import sys
import csv
import panda
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
    raise SystemExit("Tag required as argument.")

##download new posts:
for post in L.get_hashtag_posts(TARGET):
    username = post.owner_username
    ID = post.owner_id
    account = (f"https://www.instagram.com/{username}")

# write to CSV
    with open(f'{TARGET}-taggers-raw.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, ID, account])

        target = open(f'{TARGET}_taggers.csv', 'w')
        unique_lines = set()
        source_lines = 0
        duplicate_lines = 0
        for line in data:
            source_lines += 1
            # Strip out the junk for an easy set check, also saves memory
            line_to_check = line.strip('\r\n')
            if line_to_check in unique_lines: # Skip if line is already in set
                duplicate_lines += 1
                continue
            else: # Write if new and append stripped line to list of seen lines
		target.write(line)
		unique_lines.add(line_to_check)
        # Be nice and close out the file
        target.close()


# Let the user know what you did
print f"FINISHED: see {TARGET}_taggers.csv"
