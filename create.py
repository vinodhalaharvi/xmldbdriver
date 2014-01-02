import sqlite3, sys
con = sqlite3.connect("example.db")
cur = con.cursor()

cur.executescript("""
	create table AlertDefinition (
		rowid INTEGER,
		text TEXT,
		description TEXT,
		parent TEXT,
		enabled TEXT,
		notifyFiltered TEXT,
		frequency TEXT,
		mtime TEXT,
		active TEXT,
		id TEXT,
		count TEXT,
		ctime TEXT,
		controlFiltered TEXT,
		priority TEXT,
		name TEXT, 
		range TEXT,
		willRecover TEXT
	);


	create table AlertActionConfig (
		rowid INTEGER,
		text TEXT,
		value TEXT,
		key TEXT
	);

	create table AlertAction (
		rowid INTEGER,
		text TEXT,
		className TEXT,
		id INTEGER
	);

	create table AlertCondition (
		rowid INTEGER,
		text TEXT,
		logMatches TEXT,
		recoverId INTEGER,
		baselinePercentage TEXT,
		logLevel TEXT,
		required TEXT,
		baselineMetric TEXT,
		baselineComparator TEXT,
		baselineType TEXT,
		thresholdComparator TEXT,
		recover TEXT,
		type TEXT,
		thresholdMetric TEXT,
		thresholdValue TEXT
	);

	create table Resource (
		rowid INTEGER,
		text TEXT,
		name TEXT, 
		id INTEGER
	);
""")
sys.exit(0)

cur.executescript("""
    create table smartreports(
	id INTEGER,
	date TEXT,
	eventtext TEXT,
	session TEXT,
	session_status TEXT,
	count TEXT,
	dxa TEXT,
	status TEXT,
	server TEXT
    );
    """)
