import sqlite3, sys
con = sqlite3.connect("example.db")
cur = con.cursor()

assert len(sys.argv) >= 2, "At least one table must be provided"
tables = sys.argv[1:]
for table in tables:
	try:
		cur.executescript("""drop table %s;""" % table);
	except:
		pass
sys.exit(0);
