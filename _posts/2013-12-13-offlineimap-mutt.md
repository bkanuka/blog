---
layout: post
title: How I Use Offlineimap
description: "Using offlineimap with mutt, and working around its flaws"
modified: 2013-12-13
category: articles
tags: [mutt, code, offlineimap, tricks, script]
---

I use mutt to write my emails, and offlineimap to sync mail between my local machine and gmail.
offlineimap is buggy. 
I tried very hard to convince myself that wasn't the case, but after using it for a few months, I had to face the truth.
I'm sure it's not completely the offlineimap developers' faults, but rather the fact that they must support a seemingly infinite combination of partial IMAP implementations.
What I mean by that, is almost every mail carrier supports IMAP, but you'd be very hard pressed to one that implements everything to specification (outside of building your own).

Anyway, the main issues I found with offlineimap all had to do with offlineimap keeping the connection open.
I'm not sure exactly what the problem is, but I think it had to do with a spotty connection, timeouts, and things like that.

## Disable IDLE and autorefresh
Therefore, the first step is to make sure every time offlineimap runs, it runs once and stops.
I did this by commenting out `autorefresh`, `quick`, `idlefolders` and `holdconnectionopen` in my `.offlineimaprc` file.

## mail-sync script
Next, I made a short script to sync my mail.
Every time you call it, it waits for any running offlineimap instances to exit, and then calls offlineimap.
Using this script instead of calling offlineimap directly ensures there aren't multiple running instances (offlineimap hates that).

{% highlight bash %}
#!/bin/bash

while pkill --signal 0 offlineimap
do
    sleep 2
done
offlineimap > ~/mail-log 2>&1 &
{% endhighlight %}

Make this script and save it as `~/bin/mail-sync` and give it execute permissions.

## mail script
I'd like to be able to open mutt and have offlineimap sync my mail in the background as long as mutt is open.
At the end of the day, I should be able to close mutt and not have offlineimap syncing all night.
I also don't need to mess around with (ana)cron scripts.
I called this script `mail`.  There is already a built-in Linux command `mail`, so maybe this a bad idea, but I never used the built-in command so it hasn't bit me yet.
Name this whatever you want.

{% highlight bash %}
#!/bin/bash
while true      # run forever
do
    offlineimap > ~/mail-log 2>&1  # run offlineimap and copy log to ~/mail-log
    sleep 120   # sleep 2 minutes
done &          # run loop in background
LOOP_PID=$!     # copy PID of loop to a var
mutt            # run mutt in foreground (also waits for mutt to exit)

kill $LOOP_PID              # these two lines are a cool trick to kill the
wait $LOOP_PID 2>/dev/null  # infinite loop and hide the error that generates

mail-sync &     # sync mail once more after mutt exits
exit 0          # force script to exit "cleanly"
{% endhighlight %}

## mutt config
Occasionally I'd like to force a mail sync from inside mutt.  
I added the following line to my `.muttrc`

{% highlight bash %}
macro index,pager s '<sync-mailbox><shell-escape>mail-sync &<enter>'
{% endhighlight %}

This mutt macro saves the current mailbox and runs our mail-sync in the background, which in turn (safely) calls offlineimap.
You can choose whatever key you'd like, but I chose *s* for *sync*.


Assuming offlineimap is configured properly, and mutt is looking for mail in the right directories, you should be good to go! (but you can always keep an eye on your logs just in case :-)  )
