---
layout: post
title: Convert Mathematica Equation to Python
description: "Convert Mathematica output for use in Python"
modified: 2014-04-15
category: articles
tags: [math, code, python, mathematica]
---

I recently used Mathematica to solve a Lagrangian differential equation. 
I wish I could have used [Sage](http://www.sagemath.org/) but I was unable to find a simple way to program the Euler-Lagrange equation into a function. 
See this [bug report](http://trac.sagemath.org/ticket/6466). 
Mathematica on the other hand, came with a [reference notebook](http://library.wolfram.com/infocenter/Demos/4656/) with the Lagrangian and E-L equations built-in.

I solved the equations in Mathematica, but needed to use the resulting equations in Python code. 
I saved the notebook as a text file (using Save As) and tirmmed the resulting text file to just the parts I wanted to convert to python.
A single line of output was something like this (trimmed):
    {% raw %}
    {x[t]->1/(-1+Subscript[r, 1])^3 E^(-t-t Subscript[r, 1]) (-E^t s+E^(t+t Subscript[r, 1]) s-E^(t Subscript[r, 1]) t v-E^(t Subscript[r, 1]) y-E^(t Subscript[r, 1]) t y+E^t s Subscript[r, 1]+2 E^(t Subscript[r, 1]) s Subscript[r, 1]-3 E^(t+t Subscript[r, 1]) s Subscript[r, 1]+E^(t Subscript[r, 1]) s t Subscript[r, 1]+3 E^(t Subscript[r, 1]) t v Subscript[r, 1]+...
    {% endraw %}

To convert this long equation to Python code, I wrote a perl script with a bunch of substitution commands.

{% gist 10744247 %}

It can be run by feeding a document on stdin:
{% highlight bash %}
./nb_to_py.pl < notebook.txt
{% endhighlight %}

Considering that the variables used in Mathematica will change for every notebook, this script will have to be adapted for every use.
However, the comments should make this fairly straight-forward.

An example output [trimmed]:
{% highlight python %}1/(-1 \
+ MIX_RATE)**3 * np.exp(-t - t * MIX_RATE) * (-np.exp(t) * SCALE \
+ np.exp(t + t * MIX_RATE) * SCALE \
- np.exp(t * MIX_RATE) * t * v_old \
- np.exp(t * MIX_RATE) * ss_old \
- np.exp(t * MIX_RATE) * t * ss_old \
+ np.exp(t) * SCALE * MIX_RATE \
{% endhighlight %}

It may be worth nothing this is the first time I've used Perl. 
There may be far better ways to do this, but I wanted an excuse to learn some perl.
