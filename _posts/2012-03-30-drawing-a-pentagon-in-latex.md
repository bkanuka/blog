---
layout: post
title: Drawing a Pentagon in LaTeX
description: Using TikZ to draw a pentagon
modified: 2012-03-30
category: articles
tags: [math, latex]
---

I needed to draw a pentagon for a paper on Galois theory I'm working on. After some research, this is what I have come up with: 
<figure>
    <img src="/images/2012-03-30-drawing-a-pentagon-in-latex/penta.png">
</figure>


In the header we use TikZ: 
{% highlight latex %}\usepackage{tikz}
{% endhighlight %}

and then draw the pentagon with the following: 
    
{% highlight latex %}\begin{tikzpicture}[scale=2.2]%change the size here
    %pentagon
    \draw[ultra thick] (0,1)--(-0.9510565163,0.309017)--(-0.58778525229,-0.809017)--(0.58778525229,-0.809017)--(0.9510565163,0.309017)--cycle;
    %pentagram
    \draw[dashed, ultra thick,color=black] (-0.9510565163,0.309017)--(0.9510565163,0.309017)--(-0.58778525229,-0.809017)--(0,1)--(0.58778525229,-0.809017)--cycle;
    %label nodes
    \node [above] at (0,1) {$\alpha_1$};
    \node [right] at (0.9510565163,0.309017) {$\alpha_2$};
    \node [below right] at (0.58778525229,-0.809017) {$\alpha_3$};
    \node [below left] at (-0.58778525229,-0.809017) {$\alpha_4$};
    \node [left] at (-0.9510565163,0.309017) {$\alpha_5$};
\end{tikzpicture}
{% endhighlight %}

Hope this helps!
