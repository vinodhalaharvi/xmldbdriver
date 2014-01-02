
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

class BaseDriver(object): 
	def __init__(self, dbname):
		"""docstring for __init__"""
		self.con = sqlite3.connect(dbname)
		self.cur = self.con.cursor()

	def insert(self, row):
		"""docstring for insert"""
		(id, table, attrib, text) = row
		table = table.split("\\")[-1]
		dct = {}
		dct.update(attrib)
		dct['rowid'] = id
		dct['text'] = text
		ins_string =  "insert into %s(%s) values (%s)" % (table, ",".join(dct.keys()), ",".join("?"*len(dct.keys())))
		#print ins_string
		self.cur.execute(ins_string, dct.values())

	def selectall(self, table):
		"""docstring for selectall"""
		self.cur.execute("select * from %s" % table)
		return self.cur.fetchall()




class XMLdriver(BaseDriver):
	def __init__(self, filename, dbname):
		"""docstring for __init__"""
		self.filename = filename
		self.file = None
		self.root = None
		self.data = None
		super(XMLdriver, self).__init__(dbname)
	
	def parse(self, tag):
		"""docstring for parse"""
		self.file = open(self.filename, 'r')
		self.root = ET.parse(self.filename).getroot()
		self.data = self.root.findall(tag)

	def printxml(self, id):
		"""docstring for printxml"""
		assert self.root is not None
		for child in self.data:
			id += 1
			for e in child.iter():
				if child.attrib or child.text:
					print (id, e.tag, e.attrib, e.text)
	
	def getrows(self, id):
		"""docstring for printxml"""
		assert self.root is not None
		for child in self.data:
			id += 1
			for e in child.iter():
				if child.attrib or child.text:
					yield (id, e.tag, e.attrib, e.text)
	

if __name__ == '__main__':
	assert len(sys.argv) == 3, "scriptname.py input.xml tag"
	filename = sys.argv[1]
	tag = sys.argv[2]
	xd = XMLdriver(filename, "example.db")
	xd.parse(tag)
	for row in xd.getrows(0):
		xd.insert(row)
	xd.con.commit()
	for row in  xd.selectall(tag.split("\\")[-1]):
		print row
