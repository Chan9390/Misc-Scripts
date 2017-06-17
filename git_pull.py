#!/usr/bin/python

import os

dirs = next(os.walk('.'))[1]
for s in dirs:
	command = "cd " + s + " && git pull"
	print "[+] Pulling repo : " + s
	os.system(command)

