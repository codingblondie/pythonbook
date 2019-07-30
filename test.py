import psycopg2
con = psycopg2.connect("host = '127.0.0.1' dbname = 'vsearchlogdb' user = 'postgres'")
cursor = con.cursor()
_SQL = """insert into log (phrase,letters,ip,browser_string,results) values (%s,%s,%s,%s,%s)"""
cursor.execute(_SQL, ('hitch-hiker','xyz','127.0.0.1','Safari','set()'))
con.commit()
_SQL="""select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)
(1, datetime.datetime(2018, 7, 18, 22, 40, 30, 313455), 'hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()')
cursor.close()
con.close()
