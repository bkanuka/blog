---
title: Connect to OLAP with Python
description: Using Python run MDX or XMLA against Microsoft SSAS in Linux
modified: 2014-05-01
layout: post
category: articles
tags: [python, linux, olap, mdx, xmla]
---

I have a Linux machine I'd like to run regular QA against different data sets.
Some of our data sets have duplicate data between them (either to ease access, or because it's in a slightly different form), and I wanted to write some basic script that checks if the data is in sync.

Most of the guides for programmatically querying OLAP are written for [Mondrian](http://community.pentaho.com/projects/mondrian/) which is a great OLAP, but unfortunately we're using Microsoft SSAS OLAP.
Most of the guides for programmatically querying SSAS are written for C# running on Windows, but unfortunately this will be running on Linux.

The trick is to get SSAS to listen to HTTP [XMLA](http://en.wikipedia.org/wiki/XML_for_Analysis) queries.
XMLA is a basic XML format that basically takes an MDX query and wraps it in some XML.
The format of XMLA isn't really important though, as we won't be using XMLA directly.
What is important is that XMLA is a well documented format that any program or OS can read and write it.

Server side configuration is found in this [Technet article](http://technet.microsoft.com/en-us/library/gg492140.aspx).
Similar configurations will work on SSAS 2005 also.
After follow this steps, you should be able to connect to your OLAP using `http://your-server-ip/OLAP/msmdpump.dll` in Excel or SQL Server Management Studio.

On client side, we use the Python module simply named [olap.xmla](https://github.com/may-day/olap).
No need to install from github though; it can be installed by simply running `pip install xmla`.

After `olap.xmla` is installed, you should be able to follow the documentation at [the github page](https://github.com/may-day/olap).
Below is an example specifically for connecting to a Microsoft SSAS OLAP:

{% gist 11458189 %}
