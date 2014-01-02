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
import sys

class Parse(object):
	"""docstring for Parse"""
	def __init__(self, filename):
		super(Parse, self).__init__()
		self.filename = filename
		self.file = open(filename)

	def string(self, list):
		"""docstring for string"""
		return " ".join(list)

	def getrows(self):
		"""docstring for parse"""
		for line in self.file.readlines():
			line =  line.strip()
			tokens = line.split()
			id  = tokens[0]
			date = " ".join(tokens[1:6])
			text = tokens[7]
			session  = tokens[8]
			session_status = tokens[9]
			count =tokens[10] 
			dxa  =tokens[11]   
			status   = tokens[12]
			server = tokens[13]
			yield (id, date, text, session, session_status, count, dxa, status, server) 

	def print_data(self):
		"""docstring for print_data"""
		for tokens in self.getrows():
			print tokens



if __name__ == '__main__':
	assert len(sys.argv) == 2 
	filename = sys.argv[1]
	p = Parse(filename)
	p.print_data()

