# -*-coding:utf-8-*-

from collections import namedtuple
websites = [
	('Sohu', 'http://www.google.com/', u'张慎'),
	('Sina', 'http://www.sina.com/', u'阿诺德'),
	('Baidu', 'http://www.baidu.com/', u'邓肯'),
]
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
	website = Website._make(website)
	print website