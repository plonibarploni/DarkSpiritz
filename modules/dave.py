#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys, string, time, random, os, glob, subprocess, rlcompleter, readline
from urlparse import urlparse
from struct import pack
from lxml import etree
from sys import stdout
from subprocess import check_output

XML = "storage/logs/config.xml"
tree = etree.parse(XML)

class colors:
    W  = '\033[0m'
    R  = '\033[31m'
    G  = '\033[32m'
    O  = '\033[33m'
    B  = '\033[34m'
    P  = '\033[35m'
    C  = '\033[36m'
    GR = '\033[40m'
    GY = '\033[43m'
    GE = '\033[41m'
    GW = '\033[4m'
    HH = '\033[1m'

intname = "dark"
det = sys.argv[0]
den = det.split('.')[-2]
fin = den.split('/')[1]
fold = den.split('/')[0]
__plugin__      = "%s.py" % (fin)
RescoursesDir = os.getcwd()
dandtime = time.strftime("%H:%M:%S")

tabcomp = [
	'help',
	'exploit',
	'info',
	'back',
	'set',
	'show options',
	'options',
	'show'
	]

def completer(text, state):
    options = [x for x in tabcomp if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

def dashboard():
	try:
		line_1 = "\033[4m" + intname + "\033[0m " + fold + "(\033[31m" + fin + "\033[0m) > "
		terminal = raw_input(line_1)
		time.sleep(0.2)
		if terminal == "help":
			print ""
			print "Core Commands"
			print "============="
			print ""
			print "  Command         Description"
			print "  -------         -----------"
			print "  help            Help menu"
			print "  exploit         Launch an exploit attempt"
			print "  back            Move back from the current context"
			print "  clear           Clear Terminal Cache"
			print "  show options    Display options of config"
			print "  set             Sets a context-specific variable to a value"
			print "  info            Displays information about one or more plugins"
			print ""
			dashboard()
		elif terminal == 'back':
			exit()
		elif terminal == 'info':
			pysec = open(fold + "/" + fin + ".plugin","r").read()
			exec(pysec)

			if "info = {" in pysec:
				for i in info:
					title = i
					body = info[str(i)]
					print "\n" + str(title) + ":"
					if not isinstance(body, str):
						for value_element in body:
							print "- ", value_element
					else:
						print body
			else:
				pass
			dashboard()
		elif terminal == 'exploit':
			fincreator = open("storage/logs/finandferb.config","w")
			fincreator.write(fin + "\n")
			fincreator.write(fold)
			fincreator.close()

			fincreator = open("storage/logs/finandferb.config","r").readlines()
			pluginname = fincreator[0].strip("\n")
			foldername = fincreator[1].strip("\n")

			RescoursesDir = os.getcwd() + "/" + foldername + "/"
			sys.path.insert(0, RescoursesDir)

			direc = foldername + "/" + pluginname + ".plugin"
			xaa = open(direc,"r").read()
			exec(xaa)
			run()
		elif terminal == 'clear':
			os.system('clear')
			dashboard()
		elif terminal[0:3] == "set":
			v = str(terminal[4:].replace(" ","\n"))
			a = open("storage/logs/temp","w")
			a.write(v)
			a.close()
			b = open("storage/logs/temp","r").readlines()
			os.system("sed -i -e '/<configuration>/,/<\/configuration>/ s|<" + b[0].strip("\n") + ">[0-9a-z.]\{1,\}</" + b[0].strip("\n") + ">|<" + b[0].strip("\n") + ">" + b[1].strip("\n") + "</" + b[0].strip("\n") + ">|g' storage/logs/config.xml && rm storage/logs/temp")
			dashboard()
		elif terminal[0:12] == "show options":
			fincreator = open("storage/logs/finandferb.config","w")
			fincreator.write(fin + "\n")
			fincreator.write(fold)
			fincreator.close()
			xxxdad = open("modules/lib.py","r")
			exec(xxxdad.read())
			xxxdad.close()
			dashboard()
		else:
			None
			dashboard()
	except KeyboardInterrupt:
		sys.exit()

class ask():
    tree = etree.parse("storage/logs/config.xml")
    for b in tree.xpath("/configuration/config/*"):
        dat = "%s = '%s'" % (b.tag,b.text)
	exec(dat)

def run(cmd):
    x = check_output(cmd, shell=True)
    i = "\033[1m["+colors.G+"!]"+colors.W+""
    print i + x

def warning(msg):
    print "\033[1m"+colors.O+"[/]"+colors.W+"", msg

def fail(msg):
    print "\033[1m"+colors.R+"[!]"+colors.W+"", msg

def success(msg):
    print "\033[1m"+colors.G+"[*]"+colors.W+"", msg

def text(msg):
    print "\033[1;94m[?]\033[0m", msg
