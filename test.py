import MySQLdb
conn = MySQLdb.connect(passwd="root")
cur = conn.cursor()
cur.execute("create table foo(bar int(11))")
cur.execute("insert into foo values (1););")
cur.execute("insert into foo values (2););")
