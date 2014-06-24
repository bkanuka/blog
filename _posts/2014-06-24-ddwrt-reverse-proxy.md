---
title: Reverse Proxy DD-WRT with Apache
modified: 2014-05-24
layout: post
category: articles
---

I have a domain which points to a home server.
I use (and highly recommend) [Duck DNS](duckdns.org) for a dynamic DNS service.
For the purpose of this article, we'll assume Duck DNS is set up, and my home domain is `example.duckdns.org`.
I wanted to access my router and settings at `example.duckdns.org/ddwrt`

Apache 2.4 (included with Ubuntu 14.04) 
{% gist bkanuka/71741fc477f923054ef4 %}
