# -*- coding: utf-8 -*-
import subprocess
import sys
import string

if __name__ == "__main__":

	s=raw_input().split()

	if not s[0].isalnum():
		print "An invalid character was found in first argument"
		sys.exit()

	if len(s)>1:
		if s[1].isdigit():
			cmd = "convert -delay {} -loop 0 ".format(s[1])
		else:
			print "Second argument must be a positive integer"
			sys.exit()
	else:
		cmd ="convert -delay 50 -loop 0 "

	for x in s[0]:
		cmd += "../img/{}.png ".format(x.upper())

	cmd +="semaphore.gif"

	subprocess.call(cmd.split())