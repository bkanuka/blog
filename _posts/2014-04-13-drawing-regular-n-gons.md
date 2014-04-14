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

We start with the unit circle centered at (0,0).
The corrdinates of any point on the circle are given by:

$$
\begin{align*}
x &= \cos (t) \\
y &= \sin (t)
\end{align*}
$$

Therefore we can find the coordinates of the regular n-gon at:

$$
\begin{align*}
x &= \cos \left(k \frac{2 \pi}{n}\right) \\
y &= \sin \left(k \frac{2 \pi}{n}\right) \quad \text{where } k = 0, 1, \ldots n
\end{align*}
$$

However, this does not garuntee that the n-gon's bottom edge will be horizontal (something we'd want for a visually pleasing drawing).
To the above formula, we can apply a starting angle $$t$$ measured from the x-axis.

$$
\begin{align*}
x &= \cos \left(t + k \frac{2 \pi}{n}\right) \\
y &= \sin \left(t + k \frac{2 \pi}{n}\right)
\end{align*}
$$

Changing $$t$$ will rotate the n-gon's starting vertex.
To garuntee the bottom edge is horizontal, we rotate the starting vertex to the bottom of the unit circle, and then one half of $$ \frac{2 \pi}{n} $$, or 

$$
\begin{align*}
t &= \frac{-\pi}{2} + \frac{1}{2}\frac{2 \pi}{n} \\
  &= \frac{-\pi}{2} + \frac{\pi}{n}
\end{align*}
$$

$$
\begin{align*}
x &= \cos \left(\frac{-\pi}{2} + \frac{\pi}{n} + k \frac{2 \pi}{n}\right) \\
y &= \sin \left(\frac{-\pi}{2} + \frac{\pi}{n} + k \frac{2 \pi}{n}\right)
\end{align*}
$$

And using the trig identities,

$$
\begin{align*}
\cos \left(\frac{-\pi}{2} + \theta\right) 
    = \cos \left(-\left(\frac{\pi}{2} - \theta\right)\right) 
    = \cos \left(\frac{\pi}{2} - \theta\right) 
    = \sin (\theta) \\
\sin \left(\frac{-\pi}{2} + \theta\right) 
    = \sin \left(-\left(\frac{\pi}{2} - \theta\right)\right) 
    = -\sin \left(\frac{\pi}{2} - \theta\right) 
    = -\cos (\theta)
\end{align*}
$$

we can simplify the equations to:

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

