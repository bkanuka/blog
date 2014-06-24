---
title: Disable Touchpad When Using Trackpoint
description: Automatically disable trackpad whenever trackpoint mouse is in use.
modified: 2014-05-24
layout: post
category: articles
---

First of all, I'd like to get a naming convention out of the way.
Being that this is a public blog, I will be using the term "TrackPoint" to refer to the mouse in the middle of the keyboard.
The following XKCD offers other possible naming conventions:

![Appropriate Name](http://imgs.xkcd.com/comics/appropriate_term.png)

Maybe it's me, or maybe the configuration of my laptop (I'm actually on a Dell right now, not a Thinkpad) but whenever I use the Trackpoint mouse, I tend to tap the touchpad and make erronious clicks.
In the past I've simply disabled the touchpad, which works for me, but tends to annoy anyone else who uses my laptop - even breifly.
Plus, more than anything, I liked the challenge.

All of the solutions I found of Google were inadequate for one reason or another, so I decided to craft my own.

{% gist bkanuka/71741fc477f923054ef4 %}

To make this work for you, you'll have to set he global variables `TRACKPOINT_NAME` and `TRACKPAD_NAME`.
Run `xinput --list --name-only` to list the names of your attached input devices.

To check if a device is in use, we use the program `xxd` to read a single byte from the raw input device.
In order to do this we will make the `/dev/input` devices readable by the group `plugdev` (or any other group you belong to).
**THIS IS NOT SECURE** because it will allow anyone belonging to `plugdev` to read raw events, and it would be trivial to create something like a keylogger.
In my case, there are no other users of this laptop besides me, so I'm not too concerned about keylogging myself.

Create a file in called `/etc/udev/rules.d/99-input.rules` with the following content: 

`KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="plugdev"`

After restarting your computer, the output of `ls -l /dev/input` should look something like this:

    total 0
    drwxr-xr-x 2 root root    120 Jun 23 07:37 by-id
    drwxr-xr-x 2 root root    120 Jun 23 07:37 by-path
    crw-r----- 1 root root 13, 64 Jun 19 18:31 event0
    crw-r----- 1 root root 13, 65 Jun 19 18:31 event1
    crw-r----- 1 root root 13, 66 Jun 19 18:31 event2
    crw-r----- 1 root root 13, 67 Jun 23 07:37 event3
    crw-r----- 1 root root 13, 68 Jun 23 07:37 event4
    crw-r----- 1 root root 13, 69 Jun 19 18:31 event5
    crw-r----- 1 root root 13, 63 Jun 19 18:31 mice
    crw-r----- 1 root root 13, 32 Jun 19 18:31 mouse0

