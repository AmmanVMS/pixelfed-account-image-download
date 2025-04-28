#!/usr/bin/python3
#
# Download images from pixelfed
#
# see https://mastodonpy.readthedocs.io/en/1.3.1/#mastodon.Mastodon.account_statuses
#
#
#
import sys
import os
from mastodon import Mastodon
from urllib.request import urlretrieve
import datetime as dt

destination = sys.argv[1] # directory
server = sys.argv[2] # https://server.domain
account = sys.argv[3] # username@domain
secret = sys.argv[4] # file with api token from https://pix.toot.wales/settings/applications
fromdate = dt.datetime.strptime(sys.argv[5], "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
if account.startswith("@"):
    account = account[1:]
with open(secret) as f:
    secret = f.read().strip()

mastodon = Mastodon(
    access_token = secret,
    api_base_url = server
)

mastodon.account_verify_credentials()

users = mastodon.account_search(account)
user_id = mastodon.me()["id"]
for user in users:
    if account.startswith(user["username"]):
        user_id = user["id"]
        print("found", user["username"], user["display_name"])

assert user_id is not None, "We need someone to follow!"

statuses = mastodon.account_statuses(user_id, only_media=True)

for i, status in enumerate(statuses):
    print(i, len(status["media_attachments"]))
    if fromdate > status["created_at"]:
        print("skip [Date]")
        continue
    for img in status["media_attachments"]:
        if img["type"] != "image":
            print("skip [Type]")
            continue
        url = img["url"]
        ext = os.path.splitext(url)[1].lower()
        file = os.path.join(destination, str(img["id"]) + ext)
        if not os.path.exists(file):
            urlretrieve(url, file)
            print("downloaded", url, file)
        else:
            print("downloaded", file, "exists.")
