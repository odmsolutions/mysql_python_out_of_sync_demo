This code is to demonstrate an odd issue in python mysqldb.

The code in the first example test_out_of_sync.py came as an example of a 
parsing error in a system import trusted data.

The error message seen here:

    _mysql_exceptions.ProgrammingError: (2014, "Commands out of sync; you can't run this command now")

Was somewhat confusing. A web search turned up little to show why this
 had happened instead of the expected error.

What actual needs to happen is that the dataset buffer needs to be cleared 
for each exec.  

Run each line from the script test_in_sync.py to see the error message you 
would expect to see for the incorrectly parsed data.

    >>> import MySQLdb
    >>> conn = MySQLdb.connect(passwd="root", db="test")
    >>> cur = conn.cursor()
    >>> cur.execute("insert into foo values (1););")
    1L
    >>> cur.nextset()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python2.7/dist-packages/MySQLdb/cursors.py", line 107, in nextset
        nr = db.next_result()
    _mysql_exceptions.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 1

Note that the error isn't shown until you do nextset here. If you are doing multiple inserts, with a parsing error, you might just miss this.

The dockerfile prepares a simple environment to run this in.


