---
layout: blog
title: Blog ~ Wallrazer, Inc ~ Code and Consulting
---

# Blog

{% for post in site.posts limit:10 %}
## {{ post.title }}
<div class="content">
	{{ content }}
	<p class='meta'>published <a href="{{ post.url }}">{{ post.date | date: "%Y/%m/%d" }}</a></p>
</div>
{% endfor %}