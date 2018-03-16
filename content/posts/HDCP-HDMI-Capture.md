---
title: "HDCP HDMI Capture"
date: 2018-01-02T20:16:04-05:00
draft: false
tags: ["linux", "htpc", "automation"]
---

## Introduction

I'm working on integrating a Chromecast with Kodi.
Basically I want Kodi and my HTPC to work as a receiver, and handle all the input switching and video sources.
Everything runs through Kodi and my TV is only ever on one input.

Why? Because it gives me more control. I can put Kodi menus over a Chromecast video in the background. I can turn off the TV when it's not in use, regardless of what input it is on. I can turn my (non-HDMI) stereo on when the Chromecast goes on, etc. But most of all, it's just a goal I've had for a while to build my own home theater "receiver", and this brings me closer.

## Problem

So I want to route an HDMI signal from a Chromecast (or anything else really) through my Linux PC.
Of course I might run into a problem - HDCP.
I typically wouldn't blog about cracking or circumventing encryption, but HDCP is laughably easy to circumvent and many other blogs link to HDMI splitters that can be used.

I don't like the splitters because they're ugly and add a lot of wire clutter.

## Solution

I came across a Chinese company called [Mine Technology](http://www.szminetech.com) that manufactures a lot of HDMI devices, many of which "forget" to check for HDCP. Not all of their devices forget about HDCP, but they are easy enough to email and ask. 

I purchased an [HD887 1 CH HDMI Video Capture Card](https://www.aliexpress.com/store/product/Cheap-Selling-1080p-30fps-One-Channel-PCIE-Full-HD-Video-Audio-Capture-Card-HDMI-Media-PCI/502381_32808405631.html) from AliExpress because it was their cheapest HDMI capture option and it arrived in just a few days.

Another option is an H.264/H.265 encoder like the [E1005S H.265 HDMI Video Encoder](https://www.aliexpress.com/store/product/Mine-E-1005-H-265-HDMI-Video-Encoder-for-IPTV-Live-Stream-Broadcast-by-RTMP-HTTP/502381_32619723360.html). This will output a network stream that your Kodi box can pick up and play - and of course doesn't require a PCI slot.

Hope this helps!
