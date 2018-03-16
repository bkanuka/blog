---
title: Drawing Regular n-gons with Horizontal Bottom
date: 2014-04-17
tags: [math, python]
mathjax: true
---

We start with the unit circle centered at (0,0).
The coordinates of any point on the circle are given by:
`
$$
\begin{align*}
x &= \cos (t) \\
y &= \sin (t)
\end{align*}
$$
`
Therefore we can find the coordinates of the regular n-gon at:
`
$$
\begin{align*}
x &= \cos \left(k \frac{2 \pi}{n}\right) \\
y &= \sin \left(k \frac{2 \pi}{n}\right) \quad \text{where } k = 0, 1, \ldots n
\end{align*}
$$
`

However, this does not guarantee that the n-gon's bottom edge will be horizontal (something we'd want for a visually pleasing drawing).
To the above formula, we can apply a starting angle `$t$` measured from the x-axis.
`
$$
\begin{align*}
x &= \cos \left(t + k \frac{2 \pi}{n}\right) \\
y &= \sin \left(t + k \frac{2 \pi}{n}\right)
\end{align*}
$$
`

Changing `$t$` will rotate the n-gon's starting vertex.
To guarantee the bottom edge is horizontal, we rotate the starting vertex to the bottom of the unit circle, and then one half of `$ \frac{2 \pi}{n} $`, or 
`
$$
\begin{align*}
t &= \frac{-\pi}{2} + \frac{1}{2}\frac{2 \pi}{n} \\
  &= \frac{-\pi}{2} + \frac{\pi}{n}
\end{align*}
$$
`
`
$$
\begin{align*}
x &= \cos \left(\frac{-\pi}{2} + \frac{\pi}{n} + k \frac{2 \pi}{n}\right) \\
y &= \sin \left(\frac{-\pi}{2} + \frac{\pi}{n} + k \frac{2 \pi}{n}\right)
\end{align*}
$$
`
And using the trig identities,
`
$$
\begin{align*}
\cos \left(\frac{-\pi}{2} + \theta\right) 
    &= \cos \left(-\left(\frac{\pi}{2} - \theta\right)\right) 
    = \cos \left(\frac{\pi}{2} - \theta\right) 
    = \sin (\theta) \\
\sin \left(\frac{-\pi}{2} + \theta\right) 
    &= \sin \left(-\left(\frac{\pi}{2} - \theta\right)\right) 
    = -\sin \left(\frac{\pi}{2} - \theta\right) 
    = -\cos (\theta)
\end{align*}
$$
`
we can simplify the equations to:
`
$$
\begin{align*}
x &= \sin \left(\frac{\pi}{n} + k \frac{2 \pi}{n}\right) \\
y &= - \cos \left(\frac{\pi}{n} + k \frac{2 \pi}{n}\right)
\end{align*}
$$
`

If we are interested in drawing an n-gon with circumcircle of radius `$r$`, centered at `$(a,b)$` 
then we can simply multiply by `$r$` and add an offset.
Therefore, the vertecies of a regular n-gon (with horizontal bottom) can be found at:
`
$$
\begin{align*}
x &= a + r \sin \left(\frac{\pi}{n} + k \frac{2 \pi}{n}\right) \\
y &= b - r \cos \left(\frac{\pi}{n} + k \frac{2 \pi}{n}\right) \quad \text{where } k = 0, 1, \ldots n
\end{align*}
$$
`
