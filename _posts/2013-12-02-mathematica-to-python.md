---
layout: post
title: Convert Mathematica Equation to Python
description: "Convert Mathematica output for use in Python"
modified: 2013-12-02
category: articles
tags: [math, code, python, mathematica]
---

I recently used Mathematica to solve a Lagrangian differential equation. 
I wish I could have used [Sage](http://www.sagemath.org/) but I was unable to find a simple way to program the Euler-Lagrange equation into a function. 
See this [bug report](http://trac.sagemath.org/ticket/6466). 
Mathematica on the other hand, came with a [reference notebook](http://library.wolfram.com/infocenter/Demos/4656/) with the Lagrangian and E-L equations built-in.

I solved the equations in Mathematica, but needed to use the resulting equations in Python code. I saved the notebook as a text file and the output it generated was something like this (trimmed):
    {% raw %}
    {{x[t]->1/(-1+Subscript[r, 1])^3 E^(-t-t Subscript[r, 1]) (-E^t s+E^(t+t Subscript[r, 1]) s-E^(t Subscript[r, 1]) t v-E^(t Subscript[r, 1]) y-E^(t Subscript[r, 1]) t y+E^t s Subscript[r, 1]+2 E^(t Subscript[r, 1]) s Subscript[r, 1]-3 E^(t+t Subscript[r, 1]) s Subscript[r, 1]+E^(t Subscript[r, 1]) s t Subscript[r, 1]+3 E^(t Subscript[r, 1]) t v Subscript[r, 1]+...
    {% endraw %}

To convert this long equation to Python code, I wrote the following Perl script:
{% highlight perl %}
#!/usr/bin/perl

$r1 = "mix_rate";
$r2 = "fade_rate";
$s = "s";
$u1 = "u1";
$u2 = "NF";
$y = "ss0";
$v = "v0";

while (<>) {
    s/[^!-~\s]//g; #strip non-ascii characters
    s/{{x\[t\]->//g;
    s/}}//g;
    s/\\.?\n//g;
    s/\+\n/\+/g;
    s/\-\n/\-/g;
    s/Box//g;
    s/y/$y/g;
    s/v/$v/g;
    s/Subscript\[r, 1\]/$r1/g;
    s/Subsuperscript\[r, 1, ([0-9]+)\]/$r1**\1/g;
    s/Subscript\[r, 2\]/$r2/g;
    s/Subsuperscript\[r, 2, ([0-9]+)\]/$r2**\1/g;
    s/Subscript\[u, 1\]/$u1/g;
    s/Subsuperscript\[u, 1, ([0-9]+)\]/$u1**\1/g;
    s/Subscript\[u, 2\]/$u2/g;
    s/Subsuperscript\[u, 2, ([0-9]+)\]/$u2**\1/g;
    s/E\^\(/np.exp(/g;
    s/E\^([0-9a-z]+)/np.exp(\1)/g;
    s/\^([0-9a-z]+)/**\1/g;
    s/([0-9]+)\/([0-9]+)/(\1.0\/\2)/g;
    s/ / * /g;
    s/([^(])-/\1 - /g;
    s/(.)\+(.)/\1 + \2/g;
    print; 
    }
{% endhighlight %}

Now all I have to do is run:
{% highlight bash %}
./convert.pl < notebook.txt
{% endhighlight %}

and I get:
{% highlight python %}
1/(-1 + mix_rate)**3 * np.exp(-t - t * mix_rate) * (-np.exp(t) * s + np.exp(t + t * mix_rate) * s - np.exp(t * mix_rate) * t * v0 - np.exp(t * mix_rate) * ss0 - np.exp(t * mix_rate) * t * ss0 + np.exp(t) * s * mix_rate + ...
{% endhighlight %}

Which of course needs some line breaks, but *is* properly formatted Python code.

It may be worth nothing this is the first time I've used Perl. There may be far better ways to do this.  However, I wanted to learn some Perl, and so far I like it!
