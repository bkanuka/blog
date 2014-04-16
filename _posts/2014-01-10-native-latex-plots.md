---
layout: post
title: Native Looking matplotlib Plots in LaTeX
description: Making matplotlib plots look native to LaTeX
modified: 2014-01-10
category: articles
tags: [latex, matplotlib, latex, tricks, script]
---

I write most of my math/numerical analysis scripts in Python, and I tend to use [matplotlib](http://matplotlib.org/) for plotting.
When including a matplotlib plot in LaTeX I got the highest quality results by saving the plot as a PDF and using `\includegraphics{plot.pdf}` in LaTeX.
However, it bothered me that the plot had different fonts and font sizes than the rest of the document.
Here's how I fixed that.

## Figure Width
I always choose the size of my plots as a percentage of the text width.
For example `width=0.6\textwidth`.
This allows me to use `0.3\textwidth` for images that are going to be side-by-side and not worry about absolute sizes.
We want matplotlib to output the right size plot so we need to find what exactly the `textwidth` is and tell matplotlib.
Do this by writing `\the\textwidth` inside your LaTeX document (inside the document, *not* the preamble) and running it through `pdflatex` or whatever LaTeX engine you use.
You'll find that LaTeX will replace the command with some number.
Record this number.

## Generate Figures
For every LaTeX document that has plots, I write a script `figures.py` which creates all the plots.
Copy the following script into `figures.py` and save it into the same folder as your LaTeX document.
Replace `fig_width_pt` with whatever number you got from above.

{% gist 10796230 %}

You *must* `import matplotlib` and make any rc changes before importing `matplotlib.pyplot`.
matplotlib expresses sizes in inches, while LaTeX likes sizes to be in pt, so the first part of this script sets up sizes in matplotlib properly.
The figure height is determined by the golden ratio, which is highly aesthetic ratio (it's a good default).

## LaTeX
Running the above with `python figures.py` produces two files: `ema.pdf` and `ema.pgf`.
The PDF file is used just to have a stand-alone version of the plot and make sure everything looks right.

To incorporate the plot into LaTeX, put `\usepackage{pgf}` in the preamble and insert using `\input{ema.pgf}`.
For example:

{% highlight latex %}\documentclass{article}
\usepackage{pgf}

\begin{document}

\begin{figure}
    \caption{A simple EMA plot.\label{fig:ema1}}
    \centering
    \input{ema.pgf}
\end{figure}

\end{document}
{% endhighlight %}

<figure>
<img src="/images/ema.png">
</figure>
