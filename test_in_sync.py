import MySQLdb
conn = MySQLdb.connect(passwd="root", db="test")
cur = conn.cursor()
cur.execute("create table foo(bar int(11))")
cur.nextset()
cur.execute("insert into foo values (1););")
cur.nextset()
cur.execute("insert into foo values (2););")
cur.nextset()
