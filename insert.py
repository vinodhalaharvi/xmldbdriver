import sqlite3
import string
import utils
import sys
if __name__ == '__main__':
        assert len(sys.argv) == 2
        filename = sys.argv[1]
	p = utils.Parse(filename)
	con = sqlite3.connect("example.db")
	cur = con.cursor()
	#cur.executemany("insert into smartreports(id, date, eventtext, session, session_status, count, dxa, status, server) values (?,?,?,?,?,?,?,?,?)", p.getrows())
	#con.commit()
	cur.execute("select * from smartreports")
	print cur.fetchall()
