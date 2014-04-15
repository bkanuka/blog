---
layout: post
title: img2pdf: Merge and resize images into a PDF
description: "Using LaTeX to merge images into a PDF"
modified: 2014-04-15
category: articles
tags: [latex, code, pdf]
---

I was recently emailed a bunch of JPEG files of a scanned document.
There was a file for ever page, and the image files were very large.
I wanted to get them all in a single PDF file on letter size paper.
Because I find PDF mystical and difficult to work with, I decided to stick to tools I know - and I know LaTeX.

In no time I learned how to use the ImageMagick tool `convert` to convert to PDF.
Assuming that our original files are named `page1.jpg`, `page2.jpg`, etc. I could do:
{% highlight bash %}convert page* -format pdf merge.pdf
{% endhighlight %}
However, this made a PDF sized to the images, rather than forcing a letter size page.

Instead, I did the following.
First, I resized the images to something reasonable using `convert` (they were insanely large).
{% highlight bash %}convert page* -resize 50% -format jpg page.jpg
{% endhighlight %}
This created files `page-0.jpg` through `page-4.jpg` with smaller sizes.
Then I wrote the following script, which I called `img2pdf` which takes images files as arguments and converts to PDF.
Save the GitHub gist to a file and mark it as executable.
`img2pdf -h` has usage instructions, but it's simple enough to figure out.

{% gist 10767052 %}
