---
title: "Box Cli Download"
date: 2018-04-11T22:15:50-04:00
draft: false
---

I recently needed to download a folder from a shared Box drive programmatically. I also wanted some basic sync ability (only download the file from Box if the file has changed).

Box has created a cli that seems to work in Windows and Mac, but guess what OS I'm using.... ;-) Anyway, even if the CLI did work, I'd still need some script to call it. So I wrote my own script to do this.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib

from urllib import parse
from boxsdk import OAuth2
from boxsdk import Client

CLIENT_ID = 'YOUR_OWN_CLIENT_ID'
CLIENT_SECRET = 'YOUR_OWN_CLIENT_SECRET'
BOX_FOLDER_ID = YOUR_FOLDER_ID

DISK_PATH = '/WHERE/TO/DOWNLOAD'


def sha1_file(path):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks
    sha1 = hashlib.sha1()

    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest()


def recursive_download(f, parent=''):
    if f._item_type == 'file':
        path = os.path.join(parent, f.name)
        
        if os.path.exists(path) and f.sha1 == sha1_file(path):
            print("Skipping existing file:", path)
        else:
            print("Downloading:", path)
            with open(path, 'wb') as disk_file:
                f.download_to(disk_file)
    elif f._item_type == 'folder':
        # Must be a folder
        name = f.get().name
        path = os.path.join(parent, name)
        print("Entering Directory:", path)
        if not os.path.exists(path):
            os.makedirs(path)
        for item in f.get_items(None):
            recursive_download(item, path)
    else:
        print("Unknown item type:", f._item_type)


def main():
    print("Downloading data files to:", DISK_PATH)

    oauth = OAuth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    auth_url, csrf_token = oauth.get_authorization_url('http://127.0.0.1')

    print("Go to this url and grant access to the app:")
    print(auth_url)
    print("")
    print("You will be redirected to a page that gives you an error.")
    print("Copy and paste the whole url of that page here.")
    url = input()

    qs = parse.parse_qs(parse.urlparse(url).query)
    access_token, refresh_token = oauth.authenticate(qs['code'][0])
    client = Client(oauth)
    user = client.user().get()
    print("Authenticated as", user.login)
    print("")

    folder = client.folder(BOX_FOLDER_ID)
    recursive_download(folder, DISK_PATH)


if __name__ == "__main__":
    main()
```

So, to use this you're going to have to create a new Box App.
Go to [https://app.box.com/developers/console](https://app.box.com/developers/console) and create a new app. The app must be of the type "Partner Integration". It doesn't matter what you call it.

Then click "View App" to find your Client ID and Client Secret. 

You will also need to change the Redirect URI to `http://127.0.0.1`. You shouldn't have to change any other settings. A "Standard OAuth 2.0 (User Authentication)" will work.

To find the `BOX_FOLDER_ID` just navigate to the folder in Box, and the folder id will be in the URL.

Once you put these values into the script, you should be good to go!
