---
layout: page
permalink: /about/index.html
title: About Me
tagline: 
tags: [about]
---

I use Math and Open Source tools to find solutions to difficult problems. My Math and Physics education gave me a strong base for data science; my love of computers and programming has allowed me to apply it. Sometimes I write about Linux, scripting languages, and things I find interesting outside of work.

I have dual American and Canadian citizenship.


# Resume

## Work Experience

### **Data Analyst** - Datavalet Technologies (July 2014 - Present)

In July 2014, Datavalet acquired BOLDstreet and I was one of 6 retained as an employee. Datavalet also manages WiFi Hotspots and collects about 10 times the amount of data as BOLDstreet.

  * Redesigned the data collection backend for all departments of Datavalet, based on the Hadoop ecosystem.
      * Managed the roles and development plan for 4 team members.
      * The original design allows for collecting and analysing 50 GB of data per day, and is horizontally scalable.
      * While designing the system, I found that my design was similar to production systems at Twitter. I contacted engineers at Twitter who helped improve the design.
  * Modified a machine learning library (PyMC) to run in parallel on Spark/Hadoop.
  * Submitted a patch to close 2 bugs in Scala (now accepted into Scala upstream).
  * Created scripts for pretty-publishing documents written in Markdown or LaTeX by our dev team.


### **Data Analyst** - BOLDstreet Wireless Inc. (October 2012 - July 2014)

BOLDstreet managed thousands of WiFi Hotspots for well-known companies in Canada. WiFi usage metrics were recorded in a SQL database. An average of 3.7 million records were added each day.

  * Filed two patents regarding signal processing and estimating the location of a WiFi device using a single WiFi access point.
      * US20130167196 - System and method for remote device recognition at public hotspots
      * CA2823895 - System and method for wireless device detection, recognition and visit profiling
  * Improved a frequent SQL query which scanned 100+ million rows to require only a single row lookup.
  * Focused on improving the "additivity" of our most commonly used SQL queries. This allowed us to cache and reuse the results of previous queries (often making the difference between a taxing SQL query or a cache lookup).
      * Time based queries were broken up into discrete timeslices and added using the Inclusion-Exclusion priciple.
      * Implemented a statistical estimator (98% accurate) that allowed "unique count" queries to be added. E.g. the unique visitors to our hotspots for a week could be found by "summing" the unique visitors for each day.  This eliminated the need for costly `UNIQUE` SQL queries.
  * Created a program to predict the movement of devices on our network (based on Page Rank).
  * Implemented an algorithm to isolate the periodicities in a set of sparse, noisy measurements. This was based on a modification of the Euclidean algorithm and Fourier transforms.
  * Explored the use of Lagrangian Mechanics to predict the movement on statistical parameters over time - an unexplored topic of academic research.

### **Researcher** - Queen's University and NSERC (April 2011 - September 2011)
Co-authored a paper furthering understanding of the Laplace transform. Presented my findings at the Canadian Undergraduate Mathematics Conference at Universite Laval.

## Coding

  * Advanced ability in Python
  * Advanced ability in Bash and related tools (awk, sed, etc.)
  * Moderate ability in Scala
  * "Read and modify" ability in many other languages (C, Java, etc.)

I have been using Linux since I was 9 years old and maintain a home server (VM's, RAID, Apache, etc). My home projects tend to revolve around small electronics and home automation. 

## Education
  
**B.Sc. Honours Mathematics (Minor in Physics), Queen's University, Kingston ON.** 

### Notable Projects

**Groups of Irreducible Quintic Polynomials**
: Described a method of reducing quintic polynomials using the geometry of a five-point star.

**Groebner Basis Method of Automatic Theorem Proving**
: Explained an algorithmic method for automatically proving geometric statements.

**Beta Deflection and Spectroscopy**
: Attempted to measure the speed of light using radioactive material and household film.

## Volunteer

I am currently working with a team at the University of Ottawa, in conjunction with Health Canada, to analyse the concentration of Calcium in urine. The goal is to develop a method of detecting the onset of osteoporosis.

## Other Achievements

  * National Gold medalist in sprint canoe, and a previous member of Team Ontario
  * Tested >99.9 percentile in Mathematics.
  * I've climbed some mountains:


<figure>
    <a href="/images/black_tusk.jpg">
        <img src="/images/black_tusk.jpg">
    </a>
</figure>
     
