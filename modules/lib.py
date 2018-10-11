#!/usr/bin/python
import time
import os, sys
from lxml import etree


def folder():
	fincreator = open("storage/logs/finandferb.config","r").readlines()
	pluginname = fincreator[0].strip("\n")
	foldername = fincreator[1].strip("\n")

	RescoursesDir = os.getcwd() + "/" + foldername + "/"
	sys.path.insert(0, RescoursesDir)

	direc = foldername + "/" + pluginname + ".plugin"
	xaa = open(direc,"r").read()
	exec(xaa)

	print ""
	print fold + " options (" + fin + "):"
	print ""
	print "  [options]	[value]"
	print "  ---------	-------------"
	for c in list(init):
		tree = etree.parse("storage/logs/config.xml")
		for b in tree.xpath("/configuration/config/" + c):
			print("  {0:13s} {1:12s}".format(b.tag, b.text))
			print ""
	
folder()
