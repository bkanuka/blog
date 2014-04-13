---
layout: post
title: Drawing Regular n-gons with Horizontal Bottom
description: 
modified: 2014-04-13
category: articles
tags: [math, python]
---

I was re-reading my post on [drawing a pentagon in LaTeX]({% post_url 2012-03-30-drawing-a-pentagon-in-latex %}) and realized I never explained how I got the coordinates of the pentagon. 
I also didn't generalize the solution to drawing n-gons.
I would like to correct those issues.

We start with the unit circle centered at \$$(0,0)$$.  Now lets put in some more math:
$$
x = \cos (t)
$$

<figure>
    <img src="/images/drawing-a-pentagon-in-latex/penta.png">
</figure>

In the header we use TikZ: 
{% highlight latex %}    
\usepackage{tikz}
{% endhighlight %}

and then draw the pentagon with the following: 
    
{% highlight latex %}    
import numpy as np

def ngon(n):
    x = [np.sin(np.pi/n + (k*2*np.pi)/n) for k in range(n+1)]
    y = [-1*np.cos(np.pi/n + (k*2*np.pi)/n) for k in range(n+1)]
    return x,y
{% endhighlight %}

Hope this helps!
