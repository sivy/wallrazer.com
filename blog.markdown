---
layout: blog
title: Blog ~ Wallrazer ~ Code and Consulting
---

# Blog

{% for post in site.posts limit:10 %}
## <a href="{{ post.url }}">{{ post.title }}</a>
<div class="content">
	{{ post.content }}
	<p class='meta'>published <a href="{{ post.url }}">{{ post.date | date: "%Y/%m/%d" }}</a></p>
</div>
{% endfor %}