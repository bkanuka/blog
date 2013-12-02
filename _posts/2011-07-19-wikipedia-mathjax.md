---
layout: post
title: Wikipedia + MathJax
description: "Making math look (and work) better on Wikipedia"
modified: 2011-07-19
category: articles
tags: [math, tutorial, wikipedia]
---


I read a lot of math-centric articles on Wikipedia and I have a number of issues with how math is displayed on Wikipedia.

* Zooming into the page or the equation causes the image to blur and loose quality.
* Selecting the equation selects an image of the equation (with a white background), so copy-paste does not always have the desired results.
* Finding the LaTeX or MathML markup source for the equation is difficult or impossible.
* Searching for text on the page does not search inside the equation.
* Equations stand out as unnecessarily large.
* Text inside an equation does not adhere to the default browser font.

## MathJax

MathJax is a program written in JavaScript that displays math exactly as it should be displayed: as text, and without all the problems mentioned above. Wikipedia user [Nageh](http://en.wikipedia.org/wiki/User:Nageh) wrote an experimental port of MathJax that works for Wikipedia.

To enable MathJax in Wikipedia, do the following:


 * Log in to Wikipedia.  If you don't already have an account, you'll have to make one. You can follow the link on the top right of any Wikipedia page.
 * Go to [this page](http://en.wikipedia.org/w/index.php?title=Special:MyPage/common.js&amp;action=edit).  This is a special page that lets you edit the way any Wikipedia page is displayed.
In the large text box on that page, paste the following code:
{% highlight javascript %}
mathJax={}; 
mathJax.fontDir="http://cdn.mathjax.org/mathjax/latest/fonts"; 
importScript('User:Nageh/mathJax.js');
{% endhighlight %}
 * Press the Save Page button below the text box.
 * You may have to enter a CAPTCHA and press Save Page again. You should now see the following (but with your username):
<figure>
    <a href="/images/wikipedia_mathjax/common_js.png">
        <img src="/images/wikipedia_mathjax/common_js.png">
    </a>
</figure>
 * Go to "My preferences" near the top of the page. Then click on "Appearance".
 * Under the Math section select the box  "Leave it as TeX (for text browsers)" so that the section looks like the following: And press "Save".
<figure>
        <img src="/images/wikipedia_mathjax/leave_as_tex.png">
</figure>

You can now go to any Wikipedia math page and have equations properly displayed.
