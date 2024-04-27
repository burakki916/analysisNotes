---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: "Welcome to rakki site" 
toc: true
---
Hi
{% for page in site.Problems %}
- page.
{% endfor %}

[test](Problems/integrals)

{% assign my_variable = "tomato" %}
{{ my_variable }}
