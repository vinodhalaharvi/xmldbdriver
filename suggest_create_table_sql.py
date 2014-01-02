
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

import xml.etree.ElementTree as ET
import sqlite3
import string
import utils
import sys
class SuggestSQL(object):
	"""docstring for SuggestSQL"""
	def __init__(self, filename, tag, tablename):
		super(SuggestSQL, self).__init__()
		self.table = {}
		self.table["tablename"] = tablename
		self.filename = filename
                self.file = open(self.filename, 'r')
                self.root = ET.parse(self.filename).getroot()
                self.data = self.root.findall(tag)
		#print self.data

	def create_statement(self,):
		"""docstring for printxml"""
		for child in self.data:
			for e in child.iter(): 
				if child.attrib:
					self.table.update(child.attrib)

		result = "create table %s (\n" % self.table["tablename"]
		result += "\trowid INTEGER,\n\ttext TEXT,\n"
		count = 1 
		len_keys = len(self.table.keys())
		for key, value in self.table.items():
			if key != "tablename":
				if count < len_keys:
					result += "\t%s %s,\n" % (key, "TEXT")
				else:
					result += "\t%s %s\n" % (key, "TEXT")
			count += 1
		result += ");\n"
		print result


if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == "-h":
		print "Example Usage:\npython suggest_create_table_sql.py alerts.xml  AlertDefinition/Resource Resource\n"
		exit(0)
        assert len(sys.argv) == 4, "scriptname.py input.xml TagName table"
        filename = sys.argv[1]
        tag = sys.argv[2]
        tablename = sys.argv[3]
	ss = SuggestSQL(filename, tag, tablename)
	ss.create_statement()
