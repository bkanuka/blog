---
layout: home
description: "Math, hacks, and scripts."
tags: [Home, status, code, blog, foss]
---

### Current Stats

| **Learning** | [Scala](http://www.scala-lang.org/) |
| **Hacking** | HTC One M7 |
| **Listening** |<span id="track_title"></span> -- <span id="track_artist"></span>|

<script>
$.getJSON("http://libre.fm/2.0/?method=user.getrecenttracks&user=bkanuka&page=1&limit=1&format=json&callback=?", function(recent){
    try{
        document.getElementById("track_title").innerHTML = recent.recenttracks.track[0].name; 
        document.getElementById("track_artist").innerHTML = recent.recenttracks.track[0].artist["#text"]; 
        }
    catch(err){
        document.getElementById("track_title").innerHTML = recent.recenttracks.track.name; 
        document.getElementById("track_artist").innerHTML = recent.recenttracks.track.artist["#text"]; 
        }
        
});
</script>
