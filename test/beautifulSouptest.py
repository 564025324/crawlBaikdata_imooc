# coding:utf-8
from bs4 import BeautifulSoup
'''html = """
<html><head><title>The Dormouse's story[title]</title></head>
<body>
<p class="title" name="first_p"><b>The Dormouse's story[p]</b></p>
<p class="story" name="sec_p">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#soup = BeautifulSoup(html,'html.parser')

#print(soup.p.contents)
#print(soup.p.attrs['name'])
#print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.p)
#print(soup.p["class"])
#print(soup.a)
#print(soup.find_all('a'))
#print(soup.find(id='link3')

---------------- 分界线-------------'''

html_doc='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for ul in soup.select('ul'):
    print(ul.attrs['id'])
    #print(ul['id'])
    #print(li.get_text())

#print(soup.select('li'))
#print(soup.select('#list-2 .element'))
#print(soup.find_all(text='Foo'))
#print(soup.find_all(attrs={'id': 'list-1'}))
#print(soup.find_all(attrs={'name': 'elements'}))