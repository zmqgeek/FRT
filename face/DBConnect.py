import MySQLdb
def dbconnect():
	conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='FRT',charset="utf8")
	return conn
