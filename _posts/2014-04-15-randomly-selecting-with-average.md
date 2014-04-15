---
layout: post
title: Randomly Selecting with Average
description: Selecting numbers from a set to make pre-defined average
modified: 2014-04-15
category: articles
tags: [math, python, algorithm]
---

We start by figuring out if I can use a gist in my article:

{% gist 10692062 %}

$$
\begin{align*}
x &= \sin \left(\frac{\pi}{n} + k \frac{2 \pi}{n}\right) \\
y &= - \cos \left(\frac{\pi}{n} + k \frac{2 \pi}{n}\right)
\end{align*}
$$


{% highlight python %}import numpy as np

def ngon(n):
    x = [np.sin(np.pi/n + (k*2*np.pi)/n) for k in range(n+1)]
    y = [-1*np.cos(np.pi/n + (k*2*np.pi)/n) for k in range(n+1)]
    return x,y
{% endhighlight %}

