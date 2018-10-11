import os, sys

from lxml import etree

def show():
    print "Configuration Settings"
    print "======================"
    print ""
    print "  Variable          Value"
    print "  --------          -----"
    XML = "storage/logs/config.xml"
    version_open = open("storage/version","r")
    version = version_open.read()
    tree = etree.parse(XML)
    for x in tree.xpath("/configuration/config/*"):
        data = "%s" % (x.text)
        ddisaslut = "%s" % (x.tag)
	for i in data.split():
		for l in ddisaslut.split():
			print("  {0:17s} {1:12s}".format(l, i))
	#print "  " + x.tag + "            " + x.text
    print ""

show()
