#!/usr/bin/python -d
import sys
try:
	from lxml import etree
except ImportError:
	print("import lxml.etree failed")
	quit()

if len(sys.argv) == 1:
	print("\nUsage: view.py <Filename.xml>\n\n")
	quit()

style = open('viewcrawl.xsl')
xslt_content = style.read()
xslt_root = etree.XML(xslt_content)
dom = etree.parse(str(sys.argv[1]))
transform = etree.XSLT(xslt_root)
result = transform(dom)
print(str(result))
quit()
