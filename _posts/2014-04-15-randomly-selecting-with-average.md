---
layout: post
title: Randomly Selecting with Average
description: Selecting numbers from a set to make pre-defined average
modified: 2014-04-15
category: articles
tags: [math, python, algorithm]
---

The goal of this project was to "randomly" select numbers from a predefined set, with replacement, in a way that the mean of the selected numbers would equal (or come close to) a specified number.
For example, and the original motivation, was to select 100 numbers from the set: $$ X = \left\{0, 0.1, 0.25, 0.5, 0.75, 0.8, 1.0\right\} $$
so that the mean of the selected numbers was $$ \approx 0.75 $$

Said a different way, given $$ n \in \mathbb{N}, X = \left\{x_1, x_2, \ldots, x_m\right\} $$ and $$ \mu $$, find $$ a_1, a_2, \ldots, a_m \in \mathbb{N}$$ such that:

$$ \frac{a_1 x_1 + a_2 x_2 + \ldots + a_m x_m}{a_1 + a_2 + \ldots + a_m} \approx \mu \quad \text{and} \\
~\\
a_1 + a_2 + \ldots + a_m = n
$$

Now obviously, this isn't something that can be solved determinstically, and there might be many different ways of selecting our $$ a_i $$.
For example, consider $$ X = [0, 0.5, 1.0] $$, $$ \mu = 0.5 $$, and $$ n = 20 $$.
We would be right to select 20 "0.5"s, or 10 "0"s and 10 "1.0"s.
Both methods would create a mean exactly equal to 0.5.
Therefore, it would be nice to have some sort of parameter that determined the "shape" of our selection, whether the selection was all from the extremes, or tightly grouped around the mean.

In order to solve both these issues, I decided to randomly select numbers from a probability distribution with finite support on $$ [\min(X), \max(X)] $$ and round to the nearest $$ x \in X $$.  
Consider the [beta distribution](http://en.wikipedia.org/wiki/Beta_distribution) 

$$ f(x;\alpha,\beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{\int_0^1 u^{\alpha-1} (1-u)^{\beta-1}\, du} $$

where $$ \alpha > 0 $$ and $$ \beta > 0 $$.
The beta distribution is a nice choice for this problem for two reasons. 
First is because of its finite support on the interval $$ [0, 1] $$.
Second, it's mean is very easy to calculate.

$$ \mu = \frac{\alpha}{\alpha + \beta} $$

This means we can intellegently select $$ \alpha $$ and $$ \beta $$ (or select one and fix the other using the above), select random numbers, round to the nearest 

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

