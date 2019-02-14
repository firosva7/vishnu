import MySQLdb
db=MySQLdb.connect (host="localhost",user="",passwd="",db="mob1")
cursor=db.cursor()
cursor.execute("CREATE TABLE mobile(MOBNAME CHAR(20) NOT NULL,RATE INT,COLOR CHAR(10),NEWRELEASE CHAR(1));")
cursor.execute("INSERT INTO mobile VALUES('SAMSUNG',24000,'BLACK','Y');")
cursor.execute("INSERT INTO mobile VALUES('IPHONE',25000,'SILVER','Y');")
cursor.execute("INSERT INTO mobile VALUES('VIVO',15000,'WHITE','N'):")
cursor.execute("INSERT INTO mobile VALUES('NOKIA',10000,'BLUE','N'):")
cursor.execute("SELECT * FROM mobile;")
print "success"
s=cursor.fetchall()
for i in s:
	print '{0:4}|{1:3}|{2:2}|{3:5}'.format(i[0],i[1],i[2],i[3])
db.commit()
db.close                    
