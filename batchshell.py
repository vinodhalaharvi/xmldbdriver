# Copyright (c) 2013, RTP Network Services, Inc.
# All Rights Reserved      (904-236-6993)
# Vinod Halaharvi / vinod.halaharvi@rtpnet.net, vinod.halaharvi@gmail.com
# 
# http://www.rtpnet.net / codesupport@rtpnet.net
#
# There is NO warranty for this software.  If this software is used by
# someone else and passed on, the recipients should know that what they
# have is not the original, so that any problems introduced by others will
# not reflect on the original authors' reputations. This is *not* authorization
# to copy or distribute this software to others!

import sqlite3
import sys
con = sqlite3.connect("example.db")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print "Enter your SQL commands to execute in sqlite3."
print "Enter quit to exit."

buffer = sys.stdin.read()

if sqlite3.complete_statement(buffer):
	try:
		buffer = buffer.strip()
		cur.execute(buffer)
		if buffer.lstrip().upper().startswith("SELECT"):
			for row in  cur.fetchall():
				print row
	except sqlite3.Error as e:
		print "An error occurred:", e.args[0]

con.close()
