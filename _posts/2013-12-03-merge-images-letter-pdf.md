---
layout: post
title: Merge images into letter size PDF
description: "Using LaTeX to merge images into a PDF"
modified: 2013-12-03
category: articles
tags: [latex, code, pdf]
---

This is a article on *one way* to do things.  There are probably people out there who can think of 10 better ways to do this.
However, I find PDF a magical, difficult to work with file format, so I tend to stick to tools I know - and I know LaTeX.

I had a number of JPG images from a scanner, that I wanted to convert to a PDF with letter size pages.
In no time I learned how to use the ImageMagick tool `convert` to convert to PDF.
{% highlight bash %}
convert page* -format pdf merge.pdf
{% endhighlight %}
However, this made a PDF sized to the images.

Instead, I did the following.  First, I resized the images to something reasonable using `convert`.
{% highlight bash %}
convert page* -resize 50% -format jpg page.jpg
{% endhighlight %}
this created files `page-0.jpg` through `page-4.jpg` with smaller sizes.  Then I wrote the following LaTeX doc:
{% highlight latex %}
\documentclass{article}
\pagestyle{empty}
\usepackage[letterpaper,margin=0.0cm]{geometry}
\usepackage{graphicx}

% If blank pages are being created, change
%   height=\textheight  to   \width=\textwidth
%\includegraphics[width=\textwidth]{page-0.jpg}
%\newpage

\begin{document}
    \includegraphics[height=\textheight]{page-0.jpg}
    \newpage
    \includegraphics[height=\textheight]{page-1.jpg}
    \newpage
    \includegraphics[height=\textheight]{page-2.jpg}
    \newpage
    \includegraphics[height=\textheight]{page-3.jpg}
    \newpage
    \includegraphics[height=\textheight]{page-4.jpg}
    \newpage
\end{document}
{% endhighlight %}

Now just running `pdflatex` creates a PDF with properly sized images, centered on a letter size page.  Perfect.
